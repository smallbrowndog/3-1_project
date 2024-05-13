import json
import pandas as pd
import matplotlib.pyplot as plt

amazon_review = pd.read_json('C:/Users/김기주/3-1project/data/Amazon_Fashion.jsonl', lines=True)

amazon_meta = pd.read_json('C:/Users/김기주/3-1project/data/meta_Amazon_Fashion.jsonl', lines=True)

print(amazon_review.columns)

print(amazon_meta.columns)

amazon_review.to_csv('C:/Users/김기주/3-1project/data/amazon_review.csv')

amazon_meta.to_csv('C:/Users/김기주/3-1project/data/amazon_meta.csv')

num = len(amazon_review['asin'].unique().tolist())
print('제품 종류:',num,'개')

num = len(amazon_review['parent_asin'].unique().tolist())
print('카테고리 종류:',num,'개')


# histo = amazon_review['asin']

# 제품별 리뷰 많은 순서대로 15개를 자르면 2만건이 됨
# sum(amazon_review['asin'].value_counts(ascending=False).head(15))
print(amazon_review['parent_asin'].value_counts(ascending=False).head(50))
print(amazon_meta[['rating_number', 'average_rating', 'parent_asin']].value_counts(ascending=False).head(50))