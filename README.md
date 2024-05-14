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

- [2-1 원시 데이터 및 데이터 구성](#2-1-원시-데이터-및-데이터-구성)

- [2-2 추출한 데이터](#2-2-추출한-데이터)

- [2-3 추출한 데이터에 대한 탐색적 데이터 분석](#2-3-추출한-데이터에-대한-탐색적-데이터-분석)

[3. 학습 데이터 구축](#3-학습-데이터-구축)

[4. MobileBERT 학습 결과](#4-MobileBERT-학습-결과)

[5. 느낀점 및 배운점](#5-느낀점-및-배운점)

</details>


## 1. 개요
### 1-1 아마존
아마존은 세계 최대의 전자상거래(=이커머스, E-commerce) 기업이자 클라우드 서비스 시장에서 1위의 점유율을 가진 기업입니다. 세계 최대의 전자상거래 기업답게 아마존 매출의 대부분은 전자상거래와 관련하여 발생합니다. 아마존의 매출 구성을 통해 이를 살펴보겠습니다.  
<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/d7527563-be5d-4ed1-9420-6fc1a81fa04e">  
아마존의 매출 중 가장 큰 비중을 차지하는 것은 단연 압도적으로 Online stores 부문입니다. 아마존은 자사의 이커머스 사이트인 amazon.com을 통해서 전자상거래 서비스를 제공하는 기업입니다. 여기서 발생한 매출 중 타사의 입점 제품을 제외한 모든 매출은 Online stores 부문의 매출로 기록됩니다. 2022년을 기준으로 약 220B(십억) 달러의 매출을 기록하였으며, 이는 전체 매출 약 513B달러의 매출에서 42% 정도에 해당하는 금액입니다.  
<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/673773c0-9a64-47d2-975d-30f0615e9c3d">  
아마존의 주력 전자상거래 시장인 미국 시장(참고로 말하자면 아마존의 국가 별 매출 비중에서 미국은 2022년 기준 69.3%입니다.)에서 아마존은 2022년을 기준으로 37.8%의 점유율을 기록하였습니다. 이는 2위인 월마트(Walmart)의 6.3%와 비교하면 압도적인 차이는 가진 점유율입니다. 미국 전자상거래 시장에서 압도적인 점유율로 1위인 아마존으로 점점 더 많은 서드파티 판매자들의 입점이 몰릴 수 밖에 없는 상황인 것입니다.  

[[출처 : Insight and Analysis 티스토리]](https://inevitablen.tistory.com/entry/%EC%95%84%EB%A7%88%EC%A1%B4Amazon-AMZN-%EA%B8%B0%EC%97%85-%EB%B6%84%EC%84%9D)  

### 1-2 리뷰가 제품 구매에 끼치는 영향

어떤 제품이든지 리뷰가 제품 구매에 끼치는 영향은 아주 크다고 할 수 있습니다.
리뷰는 바로 브랜드가 직접 만들 수 없습니다.
때문에 어떠한 제품에 양질의 리뷰, 좋지 않은 리뷰가 많다는 것은 그 제품에 대한 다수의 평가지표로 쓰일 수 있다는 것을 의미합니다.
리뷰 작성은 전체 구매자 중에서도 일부만이 참여하며 그 중에서도 구매에 영향을 주는 좋은 리뷰를 남기는 수는 더욱 적기 때문입니다.
하지만 수집이 어려운 만큼 좋은 리뷰 콘텐츠의 영향력은 어마어마 합니다.  
<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/0a8cc91f-2492-47c7-aeac-29a43359e69a" width="800" height="417">  
위 사진처럼 한국소비자원의 조사에 따르면 무려 97%의 소비자들이 구매 결정 과정에서 검토하는 콘텐츠로 리뷰를 선정했고, 72.4%의 소비자가 충분한 리뷰가 없다면 상품을 구매하지 않는다고 답변했습니다.  
[[출처 : 브이리뷰 / 쇼핑몰 리뷰가 구매 전환율에 정말 도움을 주나요?]](https://vreview.tv/blog/content/review-marketing-1)

이번 프로젝트에서는 아마존 패션 카테고리의 리뷰들을 이용해 리뷰 데이터의 정확도와 긍, 부정 예측을 시작해보고자 한다.

## 2. 데이터
### 2-1 원시 데이터 및 데이터 구성

[아마존 리뷰 데이터](https://amazon-reviews-2023.github.io/)

- 데이터 정보  
  이용한 데이터는 'Amazon_Fashion' 데이터중 'review' 를 사용하였고 1996년 4월부터 2023년 9월까지 작성된 아마존 제품의 리뷰가 모두 작성되어있는 데이터이다.

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

데이터를 확인해보니 총 2,500,939건의 데이터로 데이터의 간소화가 필요했다.  

### 2-2 추출한 데이터

우선 실 구매자가 아닌 리뷰어의 데이터를 삭제하여 리뷰의 신뢰성을 높이며 데이터의 수를 줄이고자 하였고
이 과정을 통해 기존 2,500,939건에서 2,337,702건으로 약 16만건의 데이터를 삭제하였다.  

이후에는 카테고리가 맞는 제품들을 선택하여 추출해 제품의 카테고리를 일치화 시키는 것과 리뷰데이터의 수도 유지하는 것이 중요하다고 생각했다.
그래서 대분류라고 할 수 있는 parent_asin에 따른 갯수들을 내림차순으로 정렬해서 50개를 추출하였고,
각각의 아래에 정리된 parent_asin을 모두 검색하여 어떤 제품인지 살펴보았다.  

| parent_asin | 개수 |            |      |            |      |            |      |            |      |
|-------------|------|------------|------|------------|------|------------|------|------------|------|
| B09TXZHKLG  | 7202 | B07JWLTCLX | 1820 | B0B2KL8C8Q | 1236 | B09JB3B36S | 1062 | B07CM4C9BD | 845  |
| B09KHSM7BB  | 6206 | B0BVMLJTFS | 1616 | B07Q2QT2SK | 1212 | B0928FSGGD | 1051 | B07PHW2CWH | 823  |
| B09M6X79V9  | 4033 | B0C4WSH5LC | 1549 | B088K6Y2WG | 1187 | B07FCW972S | 1032 | B076MYYDLZ | 803  |
| B07GKLQ5KV  | 3364 | B09Y3TXYF1 | 1509 | B079RMS9ZG | 1164 | B09MJ6NSNM | 1022 | B07YSSNLSW | 788  |
| B09H6MXJ71  | 3084 | B0045H0L1W | 1482 | B06XWK1RCB | 1164 | B084LJ5ZJ5 | 953  | B01JUP0DLQ | 784  |
| B084RYPGXN  | 2600 | B07VPGY6FX | 1375 | B0B16Q1854 | 1160 | B097RFTKJP | 899  | B07BJ9G6Q9 | 765  |
| B09WJSHQFL  | 2474 | B01GKAEC6Q | 1348 | B009R09Z8W | 1140 | B0BL8ZHRMZ | 898  | B07S8KMCQW | 751  |
| B09QFJGKM5  | 2354 | B0C3G9447V | 1345 | B09TXPYLQF | 1084 | B07BMCRRYG | 884  | B00QETU2MM | 750  |
| B07CQ84KLT  | 2060 | B08F1V3KB9 | 1338 | B0B12PBSTG | 1071 | B0B14FJ5SS | 876  | B08HM3Y85H | 748  |
| B07BM9GWG7  | 1945 | B06W57G8QX | 1265 | B0871C2SJJ | 1071 | B07XD71F1H | 859  | B076QD9NP1 | 741  |




아마존 사이트에서 직접 검색을 통해 원피스, 후드티, 바지 등의 의류들만 모아 다시 데이터를 정했고 images, user_id, verified_purchase는 삭제하여 새로운 데이터셋을 만들었다.  


|       | rating | title                                             | text                                              | asin       | parent_asin | timestamp               | helpful_vote  |
|-------|--------|---------------------------------------------------|---------------------------------------------------|------------|-------------|-------------------------|---------------|
| 0     | 5      | Great! Great!                                     | I absolutely love the color and the thickness.... | B0147ZXS5W | B009R09Z8W  | 2019-02-21 06:47:03.912 | 0             |
| 1     | 4      | thinner than I would like, but fair for the price | thinner than I would like, but fair for the pr... | B00OEF1Q9G | B009R09Z8W  | 2015-02-03 21:50:44.000 | 0             |
| 2     | 5      | Hoddies                                           | These are my favorite hoodies. I must have 12 ... | B00OEZ3716 | B009R09Z8W  | 2022-03-24 16:44:26.591 | 0             |
| 3     | 5      | Great fit                                         | Love the color and fits well.                     | B00O558WWY | B009R09Z8W  | 2021-06-01 11:48:58.968 | 1             |
| 4     | 5      | My son loves it.                                  | My son loves it and wears it constantly. Beefy... | B00MNNIYRS | B009R09Z8W  | 2016-01-13 05:37:58.000 | 0             |
| ...   | ...    | ...                                               | ...                                               | ...        | ...         | ...                     | ...           |
| 28966 | 2      | Not worth it.                                     | This product was shown as a hot pink pant legg... | B07MHK3FFL | B0BVMLJTFS  | 2020-07-20 14:44:09.297 | 0             |
| 28967 | 5      | Great for working out for lounging!               | Perfect dupes!                                    | B099F6J13V | B0BVMLJTFS  | 2022-03-06 19:16:36.298 | 0             |
| 28968 | 5      | Buy them                                          | I don’t often leave reviews but I love these s... | B08PXQFPZH | B0BVMLJTFS  | 2023-01-16 14:38:12.693 | 0             |
| 28969 | 5      | Nice!                                             | Super comfy and not see through. Very flatteri... | B07S8PNPM4 | B0BVMLJTFS  | 2019-12-08 03:47:03.011 | 0             |
| 28970 | 5      | Happy                                             | Very happy with my delivery and item              | B07S8PNPM4 | B0BVMLJTFS  | 2021-02-07 19:21:37.995 | 0             |

28971 rows × 7 columns

기존 2,337,702건의 데이터에서 28,971건의 데이터로 추려내었다.  


### 2-3 추출한 데이터에 대한 탐색적 데이터 분석


위에서 추출한 데이터를 토대로 리뷰의 분포 및 리뷰 본문의 길이를 확인해보았다.  

<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/3dfa2ced-8ad4-4100-a654-a8bdb83cf0e1">  

5점을 부여한 데이터가 많은 것으로보아 대부분의 사람들은 높은 점수의 리뷰를 작성한다라는 것을 알 수 있었다.  


<img src="https://github.com/smallbrowndog/3-1_project/assets/136410944/d8b57e69-f6b4-4e1f-b424-4034aa426755">  

위 표를 확인하면 50자 이하의 리뷰가 가장 많았고 더 많은 글자를 작성하는 인원의 수는 감소세를 보이고 있다.  



## 3. 학습 데이터 구축

## 4. MobileBERT 학습 결과

## 5. 느낀점 및 배운점
