import pandas as pd
from transformers import MobileBertForSequenceClassification, MobileBertTokenizer
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import TensorDataset, Dataset, RandomSampler, SequentialSampler, DataLoader
import numpy as np
from transformers import get_linear_schedule_with_warmup, logging
import time
import datetime

# PA_fin_df = pd.read_csv('project.csv')
# PA_fin_df['tot_text'] = np.where(PA_fin_df['text'].isna(), PA_fin_df['title'],
#                                 PA_fin_df['title'] + ' ' + PA_fin_df['text'])
# filtered_df = PA_fin_df.dropna(subset=['tot_text'])
# # 열 삭제 후 새 DataFrame 생성
# df_without_cols = filtered_df.drop(['title', 'text', 'Unnamed: 0'], axis=1)
# # 수정된 DataFrame을 filtered_df에 할당
# filtered_df = df_without_cols
# filtered_df.to_csv('project_tot_text.csv')
path = "train_percent.csv"
df = pd.read_csv(path)

# 입력이 될 데이터
data_X = list(df['tot_text'].values)
labels = df['pos_neg'].values

print("*** 데이터 ***")
print("문장")
print(data_X[:5])
# 아래 방법처럼 한 줄 안에 코드를 여러개 작성할 수 있음
print("라벨"); print(labels[:5])

# 데이터 토큰화
num_to_print = 3

# do_lower_case > 모든 단어를 소문자로 변환
tokenizer = MobileBertTokenizer.from_pretrained('mobilebert-uncased', do_lower_case = True)

# 문장을 적절한 단위로 자르기
# truncation=True > 토큰의 개수 지정
# max_length=N > N개 이상의 토큰이면 그 뒤는 다 날려버림
# add_special_tokens=True > 시작과 끝을 나타내는 토큰을 넣겠다 시작: [CLS] 끝: [SEP]
# padding="max_length" > max_length개가 될때까지 나머지를 0으로 채운다
inputs = tokenizer(data_X, truncation=True, max_length=256, add_special_tokens=True, padding="max_length")
input_ids = inputs['input_ids']
# attention_mask > 단어가 있는 영역은 1, 단어가 없는 영역은 0으로 변환하여 연산이 쉽도록 함
attention_mask = inputs['attention_mask']
print("\n\n*** 토큰화 ***")
for j in range(num_to_print):
    print(f"\n{j+1}번째 데이터")
    print("** 토큰 **")
    print(input_ids[j])
    print("** 어텐션 마스크 **")
    print(attention_mask[j])
# 이미 교육된 데이터를 토대로 만들기때문에 없는 단어가 있을 수 있음

# 데이터 나누기, 0.1퍼센트는 train으로, 나머지는 validation으로 들어갈 수 있도록 함
train, validation, train_y, validation_y = train_test_split(input_ids, labels, test_size=0.1, random_state=2024)
train_masks, validation_masks, _, _ = train_test_split(attention_mask, labels, test_size=0.1, random_state=2024)

# 배치사이즈가 크면 클수록 많은 내용을 한꺼번에 계산할 수 있지만 연산량이 늘어남, 한꺼번에 학습할 데이터의 양(900개가 있으면 8로 나누어서 한번에 학습하는것)
batch_size = 8
train_inputs = torch.tensor(train)
train_labels = torch.tensor(train_y)
train_masks  = torch.tensor(train_masks)
# 하나의 데이터로 합치는 과정
train_data   = TensorDataset(train_inputs, train_masks, train_labels)
# 랜덤으로 샘플 데이터를 추출
train_sampler = RandomSampler(train_data)
# 배치사이즈만큼 가져와서 섞어주는것
train_dataloader = DataLoader(train_data, sampler=train_sampler, batch_size=batch_size)

# 검증 데이터셋
validation_inputs = torch.tensor(validation)
validation_labels = torch.tensor(validation_y)
validation_masks  = torch.tensor(validation_masks)
validation_data   = TensorDataset(validation_inputs, validation_masks, validation_labels)
validation_sampler = SequentialSampler(validation_data)
validation_dataloader = DataLoader(validation_data, sampler=validation_sampler, batch_size=batch_size)

model = MobileBertForSequenceClassification.from_pretrained('mobilebert-uncased', num_labels = 2)

# 학습 알고리즘 설치, lr은 이미 학습된 데이터이기때문에 적게 잡아도 됨
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5, eps=1e-8)

# 반복횟수
epoch = 4
# 이미 학습된 모델이기때문에 가중치가 고정되어있는데 그것을 변경하기 위해서 학습률을 조정하는것
# train_dataloader는 현재 113개임
scheduler = get_linear_schedule_with_warmup(optimizer,
                                            num_warmup_steps=0,
                                            num_training_steps=len(train_dataloader) * epoch)

for e in range(0, epoch):
    print(f'\n\nEpoch {e+1} / {epoch}')
    print('Training')
    t0 = time.time()
    total_loss = 0
    # 학습모드로 변경
    model.train()


    for step, batch in enumerate(train_dataloader):
        # 0번째가 아니고 매 50번째마다의 걸린 시간을 출력
        if step % 50 == 0 and not step == 0:
            # 시간 차이를 저장
            elapsed_rounded = int(round(time.time() - t0))
            # 시간 차이를 시간, 분, 초 단위로 변경해주는것
            elapsed = str(datetime.timedelta(seconds=elapsed_rounded))
            print(f'- Batch {step} of {len(train_dataloader)}, Elapsed time: {elapsed}')

        # train_dataloader가 batch가 되고 각각에 대응하는 ids, mask, labels를 추출
        batch_ids, batch_mask, batch_labels = tuple(t for t in batch)
        # 최적화
        model.zero_grad()

        # 결과 계산
        outputs = model(batch_ids, token_type_ids=None, attention_mask=batch_mask, labels=batch_labels)

        # loss 계산
        loss = outputs.loss
        total_loss += loss.item()

        # 10번째마다 loss 출력
        if step % 10 == 0 and not step == 0:
            print(f'Step: {step}, loss: {loss.item()}')

        # 역전파
        loss.backward()
        # 재학습 최적화를 위한 코드
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        # 실제로 모수 조정을 하게 되는것
        optimizer.step()
        # 학습률 조정
        scheduler.step()

    # 평균 loss 계산
    avg_train_loss = total_loss / len(train_dataloader)
    print(f'Average training loss: {avg_train_loss}')
    train_time_per_epoch = str(datetime.timedelta(seconds=(int(round(time.time() - t0)))))
    print(f'Training time of epoch {e}: {train_time_per_epoch}')

    print('\nValidation')
    # 시간 초기화
    t0 = time.time()
    # eval 모드로 변경
    model.eval()
    eval_loss, eval_accuracy, eval_step, eval_example = 0, 0, 0, 0
    for batch in validation_dataloader:
        batch_ids, batch_mask, batch_labels = tuple(t for t in batch)

        # 계산을 할때 그래디언트를 저장하면서 계산(가중치를 업데이트하기 위해서)
        with torch.no_grad():
            outputs = model(batch_ids, token_type_ids=None, attention_mask=batch_mask)

        logits = outputs[0]
        logits = logits.numpy()
        labels_ids = batch_labels.numpy()


        pred_flat = np.argmax(logits, axis=1).flatten()
        labels_flat = labels_ids.flatten()
        eval_accuracy_temp = np.sum(pred_flat == labels_flat) / len(labels_flat)
        # 정확도 계산
        eval_accuracy += eval_accuracy_temp
        eval_step += 1
    print(f'Validation accuracy: {eval_accuracy / eval_step}')
    val_time_per_epoch = str(datetime.timedelta(seconds=int(round(time.time() - t0))))
    print(f'Validation time of epoch {e}: {val_time_per_epoch}')

print(f'\n Save Model')
save_path = 'mobilebert_model_percent'
model.save_pretrained(save_path+'.pt')
print('\nFinish')