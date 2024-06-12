## MobileBERT를 활용한 아마존 패션 제품 리뷰 분석
<!-- 
badge icon 참고 사이트
https://github.com/danmadeira/simple-icon-badges
-->
<p align="center"><img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/aa832db3-679b-4a38-b144-bc95df425c1e"></p>
<div align=center><h1>📚 STACKS</h1></div>

<div align=center> 
<!--   https://simpleicons.org/
  <img src="https://img.shields.io/badge/[아이콘 검색]-[색상코드]?style=for-the-badge&logo=[아이콘 검색]&logoColor=white"> -->
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/pycharm-%23000000.svg?&style=for-the-badge&logo=pycharm&logoColor=white" />
</div>

<details>
<summary>내용 순서</summary>

[1. 개요](#1-개요)

- [1-1 아마존](#1-1-아마존)

- [1-2 리뷰가 제품 구매에 끼치는 영향](#1-2-리뷰가-제품-구매에-끼치는-영향)


[2. 데이터](#2-데이터)

- [2-1 원시 데이터 정보](#2-1-원시-데이터-정보)

- [2-2 추출한 데이터](#2-2-추출한-데이터)

- [2-3 추출한 데이터에 대한 탐색적 데이터 분석](#2-3-추출한-데이터에-대한-탐색적-데이터-분석)

[3. 학습 데이터 구축](#3-학습-데이터-구축)

[4. MobileBERT 학습 결과](#4-MobileBERT-학습-결과)

[5. 느낀점 및 배운점](#5-느낀점-및-배운점)

</details>


## 1. 개요
### 1-1 아마존
아마존은 세계 최대의 전자상거래(=이커머스, E-commerce) 기업이자 클라우드 서비스 시장에서 1위의 점유율을 가진 기업이다. 세계 최대의 전자상거래 기업답게 아마존 매출의 대부분은 전자상거래와 관련하여 발생한다. 아마존의 매출 구성을 통해 이를 살펴보겠다.  

<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/001f4a48-2f48-43ec-ba3c-0e6d09c8d241">

아마존의 매출 중 가장 큰 비중을 차지하는 것은 단연 압도적으로 Online stores 부문이다. 아마존은 자사의 이커머스 사이트인 amazon.com을 통해서 전자상거래 서비스를 제공하는 기업이다. 여기서 발생한 매출 중 타사의 입점 제품을 제외한 모든 매출은 Online stores 부문의 매출로 기록된다. 2022년을 기준으로 약 220B(십억) 달러의 매출을 기록하였으며, 이는 전체 매출 약 513B달러의 매출에서 42% 정도에 해당하는 금액이다.  
아마존의 주력 전자상거래 시장인 미국 시장(참고로 말하자면 아마존의 국가 별 매출 비중에서 미국은 2022년 기준 69.3%이다.)에서 아마존은 2022년을 기준으로 37.8%의 점유율을 기록하였다. 이는 2위인 월마트(Walmart)의 6.3%와 비교하면 압도적인 차이는 가진 점유율이다. 미국 전자상거래 시장에서 압도적인 점유율로 1위인 아마존으로 점점 더 많은 서드파티 판매자들의 입점이 몰릴 수 밖에 없는 상황인 것이다.  

[[출처 : Insight and Analysis 티스토리]](https://inevitablen.tistory.com/entry/%EC%95%84%EB%A7%88%EC%A1%B4Amazon-AMZN-%EA%B8%B0%EC%97%85-%EB%B6%84%EC%84%9D)  

### 1-2 리뷰가 제품 구매에 끼치는 영향

어떤 제품이든지 리뷰가 제품 구매에 끼치는 영향은 아주 크다고 할 수 있다.
리뷰는 바로 브랜드가 직접 만들 수 없기때문이다.
때문에 어떠한 제품에 양질의 리뷰, 좋지 않은 리뷰가 많다는 것은 그 제품에 대한 다수의 평가지표로 쓰일 수 있다는 것을 의미한다.
리뷰 작성은 전체 구매자 중에서도 일부만이 참여하며 그 중에서도 구매에 영향을 주는 좋은 리뷰를 남기는 수는 더욱 적기 때문이다.
하지만 수집이 어려운 만큼 좋은 리뷰 콘텐츠의 영향력은 매우 크다고 할수 있다.  
<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/0a8cc91f-2492-47c7-aeac-29a43359e69a" width="800" height="417">  
<!-- <img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/7c80201a-fe90-4d90-ab04-b90f04bd0d2d">   -->

위 사진처럼 한국소비자원의 조사에 따르면 무려 97%의 소비자들이 구매 결정 과정에서 검토하는 콘텐츠로 리뷰를 선정했고, 72.4%의 소비자가 충분한 리뷰가 없다면 상품을 구매하지 않는다고 답변했다.  
[[출처 : 브이리뷰 / 쇼핑몰 리뷰가 구매 전환율에 정말 도움을 주나요?]](https://vreview.tv/blog/content/review-marketing-1)

이번 프로젝트에서는 아마존 패션 카테고리의 리뷰들을 이용해 리뷰 데이터의 정확도와 긍, 부정 예측을 시작해보고자 한다.

## 2. 데이터
### 2-1 원시 데이터 정보

[아마존 리뷰 데이터](https://amazon-reviews-2023.github.io/)

- 데이터 정보  
  이용한 데이터는 위 사이트에서 제공되는 카테고리중 'Amazon_Fashion'의 'review' 를 사용하였고 1996년 4월부터 2023년 9월까지 작성된 아마존 제품의 리뷰가 모두 작성되어있는 데이터이다.

[ 데이터 구성 ]

|rating|title|text|images|asin|parent_asin|user_id|timestamp|helpful_vote|verified_purchase|
|---|---|---|---|---|---|---|---|---|---|
|리뷰 점수|리뷰 제목|리뷰 본문|리뷰 사진|제품 ID|제품 상위 ID|리뷰어 ID|리뷰 작성 시간|유용한 리뷰 투표|리뷰어 실구매 여부 확인|


[ 데이터 정보 ]

||rating|title|text|images|asin|parent_asin|user_id|timestamp|helpful_vote|verified_purchase|
|---|---|---|---|---|---|---|---|---|---|---|
|0|5|Pretty locket|I think this locket is really pretty. The insi...|[]|B00LOPVX74|B00LOPVX74|AGBFYI2DDIKXC5Y4FARTYDTQBMFQ|2020-01-09 00:06:34.489|3|True|
|1|5|A|Great|[]|B07B4JXK8D|B07B4JXK8D|AFQLNQNQYFWQZPJQZS6V3NZU4QBQ|2020-12-20 01:04:06.701|0|True|
|2|2|Two Stars|One of the stones fell out within the first 2 ...|[]|B007ZSEQ4Q|B007ZSEQ4Q|AHITBJSS7KYUBVZPX7M2WJCOIVKQ|2015-05-23 01:33:48.000|3|True|
|...|...|...|...|...|...|...|...|...|...|...|
|2500938|1|Empty plastic bag|I got an empty bag in my package of 10 that I ...|[]|B00YGFMQC0|B00YGFMQC0|AGN3P7MZ3WYZQTPOCSIWNTHD5RDQ|2017-03-15 00:25:02.000|1|True|

2500939 rows × 10 columns

데이터를 확인해보니 총 2,500,939건의 데이터이며 평점은 0~5점으로 구성되어 있다.  




### 2-2 추출한 데이터

우선 실 구매자가 아닌 리뷰어의 데이터를 삭제하여 리뷰의 신뢰성을 높이며 데이터의 수를 줄이고자 하였고
이 과정을 통해 기존 2,500,939건에서 2,337,702건으로 약 16만건의 데이터를 삭제하였다.  

이후에는 카테고리가 맞는 제품들을 선택하여 추출해 제품의 카테고리를 일치화 시키는 것과 리뷰데이터의 수도 유지하는 것이 중요하다고 생각했다.
그래서 대분류라고 할 수 있는 parent_asin에 따른 갯수들을 내림차순으로 정렬해서 50개를 추출하였고,
각각의 아래에 정리된 parent_asin을 모두 검색하여 어떤 제품인지 살펴보았다.  

| parent_asin | 개수   | 제품종류  |            |      |          |            |     |               |
|-------------|------|-------|------------|------|----------|------------|-----|---------------|
| B09TXZHKLG  | 7202 | 시계    | B0C3G9447V | 1345 | 슬리퍼      | B084LJ5ZJ5 | 953 | 후디            |
| B09KHSM7BB  | 6206 | 후디    | B08F1V3KB9 | 1338 | 레깅스      | B097RFTKJP | 899 | 원피스           |
| B09M6X79V9  | 4033 | 나시    | B06W57G8QX | 1265 | 양말       | B0BL8ZHRMZ | 898 | 안경스트랩         |
| B07GKLQ5KV  | 3364 | -     | B0B2KL8C8Q | 1236 | 긴팔 스포츠웨어 | B07BMCRRYG | 884 | 크로스백          |
| B09H6MXJ71  | 3084 | 나시    | B07Q2QT2SK | 1212 | -        | B0B14FJ5SS | 876 | -             |
| B084RYPGXN  | 2600 | -     | B088K6Y2WG | 1187 | 위생모      | B07XD71F1H | 859 | 원피스           |
| B09WJSHQFL  | 2474 | -     | B079RMS9ZG | 1164 | 안경       | B07CM4C9BD | 845 | 안경            |
| B09QFJGKM5  | 2354 | 양말    | B06XWK1RCB | 1164 | 양말       | B07PHW2CWH | 823 | 아동용 티셔츠       |
| B07CQ84KLT  | 2060 | 원피스   | B0B16Q1854 | 1160 | 조거팬츠     | B076MYYDLZ | 803 | 부츠            |
| B07BM9GWG7  | 1945 | 나시    | B009R09Z8W | 1140 | 후디       | B07YSSNLSW | 788 | 아동용 수술 후 티셔츠  |
| B07JWLTCLX  | 1820 | 비니    | B09TXPYLQF | 1084 | 백팩       | B01JUP0DLQ | 784 | 가디건           |
| B0BVMLJTFS  | 1616 | 레깅스   | B0B12PBSTG | 1071 | 헤드폰      | B07BJ9G6Q9 | 765 | 팔토시           |
| B0C4WSH5LC  | 1549 | 양말    | B0871C2SJJ | 1071 | 선글라스     | B07S8KMCQW | 751 | 나시            |
| B09Y3TXYF1  | 1509 | 신발    | B09JB3B36S | 1062 | 마스크      | B00QETU2MM | 750 | 액세서리 오거나이저    |
| B0045H0L1W  | 1482 | 손가락조명 | B0928FSGGD | 1051 | 긴팔 스포츠웨어 | B08HM3Y85H | 748 | 작업 모자         |
| B07VPGY6FX  | 1375 | 방한장갑  | B07FCW972S | 1032 | 양말       | B076QD9NP1 | 741 | 원피스           |
| B01GKAEC6Q  | 1348 | 속옷    | B09MJ6NSNM | 1022 | 나시       |            |     |               |




<!--
나시
'B09M6X79V9'
'B09H6MXJ71'
'B07BM9GWG7'
'B09MJ6NSNM'
'B07S8KMCQW'

원피스
'B07CQ84KLT'
'B097RFTKJP'
'B07XD71F1H'
'B076QD9NP1'

후디
'B09KHSM7BB'
'B009R09Z8W'
'B084LJ5ZJ5'

레깅스
'B0BVMLJTFS'
'B08F1V3KB9'

긴팔스포츠웨어
'B0B2KL8C8Q'
'B0928FSGGD'

가디건
'B01JUP0DLQ'

조거팬츠
'B0B16Q1854'
-->



아마존 사이트에서 직접 검색을 통해 원피스, 후드티, 바지 등의 의류들만 모아 다시 데이터를 정했고 images, asin, parent_asin, user_id, timestamp, verified_purchase, helpful_vote는 삭제하여 새로운 데이터셋을 만들었다.  


|       | rating | title                                | text                                              |
|-------|--------|--------------------------------------|---------------------------------------------------|
| 0     | 5      | Nice quality product                 | Great product                                     |
| 1     | 5      | Five Stars                           | Good product                                      |
| 2     | 4      | Good material, true to size          | Ordered neon green and received yellow. The sw... |
| ...   | ...    | ...                                  | ...                                               |
| 30877 | 5      | These pants are amazing              | Love these pants! So comfortable. Love the h...   |


30878 rows × 4 columns  
기존 2,337,702건의 데이터에서 30,878건의 데이터로 추려내었다.  

title, text 데이터를 살펴보니 title에도 유의미한 단어가 있고 text에는 빈 값이 존재하는걸 확인하여 tot_text로 두 열을 병합하였다.
tot_text에 있던 빈 값을 삭제하였다.

이후 3점 이하의 리뷰는 부정, 4점 이상의 리뷰는 긍정으로 분류하여 pos_neg로 추가하였다.
3점의 리뷰는 대체로 부정적인 리뷰들이 많아 부정으로 분류하였다.

|       | rating | parent_asin | pos_neg | tot_text                                          |
|-------|--------|-------------|---------|---------------------------------------------------|
| 0     | 5      | B009R09Z8W  | 1       | Nice quality product Great product                |
| 1     | 5      | B009R09Z8W  | 1       | Five Stars Good product                           |
| 2     | 4      | B009R09Z8W  | 1       | Good material, true to size Ordered neon green... |
| ...   | ...    | ...         | ...     | ...                                               |
| 30864 | 5      | B0BVMLJTFS  | 1       | These pants are amazing Love these pants! So ...  |

30865 rows × 5 columns  
위 같이 학습을 위한 데이터 전처리를 마쳤다.

### 2-3 추출한 데이터에 대한 탐색적 데이터 분석


위에서 추출한 데이터를 토대로 리뷰의 분포 및 리뷰 본문의 길이를 확인해보았다.  

<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/71f85637-676c-4119-8b81-4ba5dbb28696">  

5점을 부여한 데이터가 많은 것으로보아 대부분의 사람들은 높은 점수의 리뷰를 작성한다라는 것을 알 수 있었다.  



<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/90007d4f-ef26-4bba-a572-2d1dba56dd6a">  



위 표를 확인하면 50자 이하의 리뷰가 가장 많았고 더 많은 글자를 작성하는 인원의 수는 감소세를 보이고 있다.  



<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/ecabceee-12e3-43e4-8060-e382eefabbd3">  


긍정과 부정 리뷰의 분포를 살펴보니 3.37:1의 불균형한 모습을 볼 수 있다.




## 3. 학습 데이터 구축

위의 그래프를 확인해보면 긍정 23,826개, 부정 7,052개의 데이터가 있는걸 확인할 수 있다.
데이터가 불균형하기 때문에 긍, 부정 데이터를 동일 비율로 추출하고자 한다.
긍, 부정 70퍼센트씩 동일한 비율로 추출하여 학습데이터로 설정했다.
70퍼센트씩 추출한 학습 결과는 Validation accuracy: 0.9328304597701149으로 나왔고 임의로 각 2000개의 데이터를 추출한 학습 결과는 Validation accuracy: 0.9가 나왔다.
해당 데이터들을 활용해 학습해보겠다.

70퍼센트씩 추출해 학습하여 결과를 예측했을때는 Total Accuracy:0.9438002073075926, 각 2000개씩, 총 4000개를 추출해 학습하여 결과를 예측했을때 <img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/10a099bf-d777-4b8a-9022-2b7b5fa305d7">


## 4. MobileBERT 학습 결과

## 5. 느낀점 및 배운점
