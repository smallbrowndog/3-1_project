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

- [1-1 이 주제를 고른 이유](#11-이-주제를-고른-이유)

- [1-2 리뷰가 제품 구매에 끼치는 영향](#12-리뷰가-제품-구매에-끼치는-영향)


[2. 데이터](#2-데이터)

- [2-1 원시 데이터](#21-원시-데이터)

- [2-2 추출한 데이터](#22-추출한-데이터)

- [2-3 추출한 데이터에 대한 탐색적 데이터 분석](#23-추출한-데이터에-대한-탐색적-데이터-분석)

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

[출처 : 브이리뷰 / 쇼핑몰 리뷰가 구매 전환율에 정말 도움을 주나요?](https://vreview.tv/blog/content/review-marketing-1)

위 자료처럼 리뷰는 제품 구매에 지대한 영향을 끼치는만큼 리뷰 데이터의 정확도와 긍, 부정 예측을 시작해보고자 한다.

## 2. 데이터
### 2-1 원시 데이터 및 데이터 구성
[아마존 리뷰 데이터](https://amazon-reviews-2023.github.io/)

- 데이터 정보
  이용한 데이터는 'Amazon_Fashion' 데이터중 'review' 를 사용하였고 1996년 4월부터 2023년 9월까지 작성된 아마존 제품의 리뷰가 모두 작성되어있는 데이터이다.
  
|rating|title|text|images|asin|parent_asin|user_id|timestamp|helpful_vote|verified_purchase|
|---|---|---|---|---|---|---|---|---|---|
|리뷰 점수|리뷰 제목|리뷰 본문|리뷰 사진|제품 ID|제품 상위 ID|리뷰어 ID|리뷰 작성 시간|유용한 리뷰 투표|리뷰어 실구매 여부 확인|


기본적인 정보 : 어떠한 데이터인지, 총 데이터 건 수

### 2-2 추출한 데이터
대량의 데이터에서 관심 영역을 추출한다. (5만 ~ 10만건)
최소 2만건

### 2-3 추출한 데이터에 대한 탐색적 데이터 분석
1~5점 척도인 경우에는 분포
리뷰 문장의 길이
연도별, 장소별 등등 데이터의 부가정보를 바탕으로 데이터를 탐색 (pandas, matplotlib)

## 3. 학습 데이터 구축

## 4. MobileBERT 학습 결과

## 5. 느낀점 및 배운점
