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

- [1-1 이 주제를 고른 이유](#1-1-이-주제를-고른-이유)

- [1-2 리뷰가 제품 구매에 끼치는 영향](#1-2-리뷰가-제품-구매에-끼치는-영향)


[2. 데이터](#2-데이터)

- [2-1 원시 데이터 및 데이터 구성](#2-1-원시-데이터-및-데이터-구성)

- [2-2 추출한 데이터](#2-2-추출한-데이터)

- [2-3 추출한 데이터에 대한 탐색적 데이터 분석](#2-3-추출한-데이터에-대한-탐색적-데이터-분석)

[3. 학습 데이터 구축](#3-학습-데이터-구축)

[4. MobileBERT 학습 결과](#4-MobileBERT-학습-결과)

[5. 느낀점 및 배운점](#5-느낀점-및-배운점)

</details>


## 1. 개요
### 1-1 이 주제를 고른 이유

여러 주제를 둘러본 결과, 옷에 대한 리뷰 데이터를 분석해보는게 저의 흥미를 이끌 수 있을 것 같아 아마존 패션 제품 리뷰를 선택하게 되었습니다.  
요즘에는 오프라인 쇼핑보다 온라인 쇼핑이 더 선호 되며 리뷰도 즉각적으로 확인 할 수 있기때문에 소비자들의 구매에는 만족과 불만족을 나누는 리뷰 데이터가 중요합니다.  
또한 회사 입장에서는 소비자들의 의견을 수용하여 더 나은 제품과 서비스를 제공할 수 있기 때문에 해당 주제를 선택하게 되었습니다.  

### 1-2 리뷰가 제품 구매에 끼치는 영향

어떤 제품이든지 리뷰가 제품 구매에 끼치는 영향은 아주 크다고 할 수 있습니다.  
리뷰는 바로 브랜드가 직접 만들 수 없습니다.  
때문에 어떠한 제품에 양질의 리뷰, 좋지 않은 리뷰가 많다는 것은 그 제품에 대한 다수의 평가지표로 쓰일 수 있다는 것을 의미합니다.  
리뷰 작성은 전체 구매자 중에서도 일부만이 참여하며 그 중에서도 구매에 영향을 주는 좋은 리뷰를 남기는 수는 더욱 적기 때문입니다.  
하지만 수집이 어려운 만큼 좋은 리뷰 콘텐츠의 영향력은 어마어마 합니다.  
<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/0a8cc91f-2492-47c7-aeac-29a43359e69a" >
위 사진처럼 한국소비자원의 조사에 따르면 무려 97%의 소비자들이 구매 결정 과정에서 검토하는 콘텐츠로 리뷰를 선정했고, 72.4%의 소비자가 충분한 리뷰가 없다면 상품을 구매하지 않는다고 답변했습니다.  
[[출처 : 브이리뷰 / 쇼핑몰 리뷰가 구매 전환율에 정말 도움을 주나요?]](https://vreview.tv/blog/content/review-marketing-1)

위 자료처럼 리뷰는 제품 구매에 지대한 영향을 끼치는만큼 리뷰 데이터의 정확도와 긍, 부정 예측을 시작해보고자 합니다.

## 2. 데이터
### 2-1 원시 데이터 및 데이터 구성

[아마존 리뷰 데이터](https://amazon-reviews-2023.github.io/)

- 데이터 정보  
  이용한 데이터는 'Amazon_Fashion' 데이터중 'review' 를 사용하였고 1996년 4월부터 2023년 9월까지 작성된 아마존 제품의 리뷰가 모두 작성되어있는 데이터입니다.

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
|3|1|Won’t buy again|Crappy socks. Money wasted. Bought to wear wit...|[]|B07F2BTFS9|B07F2BTFS9|AFVNEEPDEIH5SPUN5BWC6NKL3WNQ|2018-12-31 20:57:27.095|2|True|
|4|5|I LOVE these glasses|I LOVE these glasses! They fit perfectly over...|[]|B00PKRFU4O|B00XESJTDE|AHSPLDNW5OOUK2PLH7GXLACFBZNQ|2015-08-13 14:29:26.000|0|True|
|...|...|...|...|...|...|...|...|...|...|...|
|2500934|5|... allowed them to be used to add military ri...|The tie tacks were the size that allowed them ...|[]|B00YGFMQC0|B00YGFMQC0|AFXSFD3FTZ2CLN3TYV4B63CQM5BQ|2016-06-24 20:12:38.000|0|True|
|2500935|1|Didn’t come with all ten|Says ten tie clips but o only received 7.|[]|B00YGFMQC0|B00YGFMQC0|AEH7WP5HGM6FGLSSC6GSTYUXBHGQ|2018-05-08 17:05:05.585	0	True|
|2500936|3|Not checked for quality|When I received them 2-3 of them did not open ...|[]|B00YGFMQC0|B00YGFMQC0|AEL2TSSBVLIPWQ7YVMK364DUYURQ|2016-12-17 22:28:31.000|0|True|
|2500937|5|Awesome|Great product.|[]|B00YGFMQC0|B00YGFMQC0|AGZ6IIYSPCW4YXWH6VFEOI7MTBZA|2017-04-15 17:34:26.000|1|True|
|2500938|1|Empty plastic bag|I got an empty bag in my package of 10 that I ...|[]|B00YGFMQC0|B00YGFMQC0|AGN3P7MZ3WYZQTPOCSIWNTHD5RDQ|2017-03-15 00:25:02.000|1|True|

2500939 rows × 10 columns

데이터를 확인해보니 총 2,500,939건의 데이터로 필히 데이터를 줄여야함을 알 수 있습니다.  

### 2-2 추출한 데이터

우선 실 구매자가 아닌 리뷰어의 데이터를 삭제하여 리뷰의 신뢰성을 높이며 데이터의 수를 줄이고자 하였고  
이 과정을 통해 기존 2,500,939건에서 2,337,702건으로 약 16만건의 데이터를 삭제하였습니다.  

이후에는 데이터를 줄이기 위해 1~5점의 데이터를 각각 2만건씩 추출하려고 했으나 각각 asin을 확인해보니 시계, 후드티, 바지, 필통, 악세사리 등 수 많은 카테고리의 제품들이 있었고,  
카테고리에 맞는 제품들을 선택하여 추출하여 제품의 카테고리를 일치화 시키는 것과 리뷰데이터의 수도 유지하는 것이 중요하다고 생각했습니다.  
그래서 대분류라고 할 수 있는 parent_asin에 따른 갯수들을 내림차순으로 정렬해서 50개를 추출하였고,  
각각의 parent_asin을 모두 검색하여 어떤 제품인지 살펴보았습니다.  

|parent_asin|개수|
|-|-|
|B09TXZHKLG|7202|
|B09KHSM7BB|6206|
|B09M6X79V9|4033|
|B07GKLQ5KV|3364|
|B09H6MXJ71|3084|
|B084RYPGXN|2600|
|B09WJSHQFL|2474|
|B09QFJGKM5|2354|
|B07CQ84KLT|2060|
|B07BM9GWG7|1945|
|B07JWLTCLX|1820|
|B0BVMLJTFS|1616|
|B0C4WSH5LC|1549|
|B09Y3TXYF1|1509|
|B0045H0L1W|1482|
|B07VPGY6FX|1375|
|B01GKAEC6Q|1348|
|B0C3G9447V|1345|
|B08F1V3KB9|1338|
|B06W57G8QX|1265|
|B0B2KL8C8Q|1236|
|B07Q2QT2SK|1212|
|B088K6Y2WG|1187|
|B079RMS9ZG|1164|
|B06XWK1RCB|1164|
|B0B16Q1854|1160|
|B009R09Z8W|1140|
|B09TXPYLQF|1084|
|B0B12PBSTG|1071|
|B0871C2SJJ|1071|
|B09JB3B36S|1062|
|B0928FSGGD|1051|
|B07FCW972S|1032|
|B09MJ6NSNM|1022|
|B084LJ5ZJ5|953|
|B097RFTKJP|899|
|B0BL8ZHRMZ|898|
|B07BMCRRYG|884|
|B0B14FJ5SS|876|
|B07XD71F1H|859|
|B07CM4C9BD|845|
|B07PHW2CWH|823|
|B076MYYDLZ|803|
|B07YSSNLSW|788|
|B01JUP0DLQ|784|
|B07BJ9G6Q9|765|
|B07S8KMCQW|751|
|B00QETU2MM|750|
|B08HM3Y85H|748|
|B076QD9NP1|741|


parent_asin 검색을 통해 원피스, 후드티, 바지 등의 의류들만 모아 다시 데이터를 정했습니다.  



|       | rating | title                                             | text                                              | images | asin       | parent_asin | user_id                      | timestamp               | helpful_vote |
|-------|--------|---------------------------------------------------|---------------------------------------------------|--------|------------|-------------|------------------------------|-------------------------|--------------|
| 0     | 5      | Great! Great!                                     | I absolutely love the color and the thickness.... | []     | B0147ZXS5W | B009R09Z8W  | AGPST67TWB7SFRSPDXCDOB2VHELA | 2019-02-21 06:47:03.912 | 0            |
| 1     | 4      | thinner than I would like, but fair for the price | thinner than I would like, but fair for the pr... | []     | B00OEF1Q9G | B009R09Z8W  | AFUJBKHTVFITEGJPUVNGG4RBU6SQ | 2015-02-03 21:50:44.000 | 0            |
| 2     | 5      | Hoddies                                           | These are my favorite hoodies. I must have 12 ... | []     | B00OEZ3716 | B009R09Z8W  | AHYC43D3W3OSR7CSGZI2FU6IT6ZA | 2022-03-24 16:44:26.591 | 0            |
| 3     | 5      | Great fit                                         | Love the color and fits well.                     | []     | B00O558WWY | B009R09Z8W  | AG4ES4AI54GK2BFIYT7YZR3YMQXA | 2021-06-01 11:48:58.968 | 1            |
| 4     | 5      | My son loves it.                                  | My son loves it and wears it constantly. Beefy... | []     | B00MNNIYRS | B009R09Z8W  | AGNHNKWELUNPQWDEKHP6J77LF2QA | 2016-01-13 05:37:58.000 | 0            |
| ...   | ...    | ...                                               | ...                                               | ...    | ...        | ...         | ...                          | ...                     | ...          |
| 28966 | 2      | Not worth it.                                     | This product was shown as a hot pink pant legg... | []     | B07MHK3FFL | B0BVMLJTFS  | AGAEEN6G7BGSKWOBNTT2QTCA2OOA | 2020-07-20 14:44:09.297 | 0            |
| 28967 | 5      | Great for working out for lounging!               | Perfect dupes!                                    | []     | B099F6J13V | B0BVMLJTFS  | AEEGB7LM7KCIQGPXP2P3QEGNCIIQ | 2022-03-06 19:16:36.298 | 0            |
| 28968 | 5      | Buy them                                          | I don’t often leave reviews but I love these s... | []     | B08PXQFPZH | B0BVMLJTFS  | AHK4BHCB4PFRBMLHSOKKZKETES4A | 2023-01-16 14:38:12.693 | 0            |



28971 rows × 10 columns

기존 2,337,702건의 데이터에서 28,971건의 데이터로 추려내었습니다.  


### 2-3 추출한 데이터에 대한 탐색적 데이터 분석


위에서 추출한 데이터를 토대로 리뷰의 분포 및 리뷰 본문의 길이를 확인해보았습니다.  

<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/3dfa2ced-8ad4-4100-a654-a8bdb83cf0e1">  

1점이 1526건, 2점이 2073건, 3점이 2510건, 4점이 4242건, 5점이 18620건 인것으로 보아 대부분의 사람들은 높은 점수의 리뷰를 작성한다라는 것을 알 수 있습니다.  


<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/6bd7f967-b2c0-4759-84a5-e212cbfab5f2">  

위 표를 확인하면 50자 이하의 리뷰가 가장 많았고 더 많은 글자를 작성하는 인원의 수는 감소세를 보이고 있습니다.  



## 3. 학습 데이터 구축

## 4. MobileBERT 학습 결과

## 5. 느낀점 및 배운점
