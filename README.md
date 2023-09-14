
# Child Carry Map - 여름철 아이들 물놀이장 장소 정보 제공 시스템

<img width="1680" alt="main" src="https://github.com/liljw/ChildCarryMap/assets/129480514/559847e1-8506-478c-8dba-5b49cde8ece5">

## 개요

본 프로젝트는 **빅데이터, AI, 클라우드 세 전공이 융합**하여 진행한 최종 프로젝트이다.  
총 5주의 시간이 주어졌으며, 주어진 시간 안에 세 전공 모두의 결과를 서비스 할 수 있는 웹 사이트를 만드는 것을 목표로 한다.  

기술 스택은 Python, Django, AWS, React, JS, HTML, CSS, MySQL 등을 사용하였다.

본 프로젝트는 총 6개 팀의 참가 가운데 **최우수상**을 수상하였다.

---

## 목차

1. 프로젝트 후기
2. 프로젝트 결과 
    - 메인페이지
    - 상세페이지
3. 기획
    - 주제 선정 배경
    - 타겟
    - 기대효과
4. 기능
    - 데이터 분석
        - 편의지수 개발
            - 데이터 마트 구축
            - 활용 데이터 셋
            - 인덱스 도출 알고리즘
            - 만족거리 및 K값
            - 회귀 모형 및 예측
            - 편의지수 도출 최종 모형
            - 편의지수 범주화
        - 시각화
            - Folium
            - 랭킹
            - 방사형차트 (스파이더넷)
    - AI 
        - 긍/부정 감성분석
            - 자연어처리
            - 딥러닝 (LSTM)
            - 감성분석 결과 예시
        - 리뷰 키워드 추출
            - 자연어처리 (워드클라우드)
5. 구현
    - 클라우드
        - 인프라 설계 구성도
    - 웹
        - 데이터베이스 ERD
6. 시연
    - 시연 영상
7. 발전 가능성
---

## 프로젝트 후기




---

## 프로젝트 결과

### 메인페이지 (Home 화면)

<img width="1680" alt="main1" src="https://github.com/liljw/ChildCarryMap/assets/129480514/56536acc-23c7-49d3-989b-6e8f4118e62d">

- 사용자가 사이트에 접속하면 보이는 메인페이지이다.
- 인터넷 브라우저가 사용자에게 위치 추적 허용 여부를 묻고, 허가한다면 **사용자의 위치**가 화면 중앙에 빨간색 네모 상자 처럼 보이게 된다. 
- 화면 상단 네비게이션 바에는 사이트의 로고와 옆으로는 (서비스 소개, 통계 한눈에 보기, 로그인/회원가입) 창으로 이동하는 버튼이 있다.
- 화면 좌측에는 **토글이 가능한 사이드 바**가 있으며, *상단의 햄버거 바를 클릭하면 사이드 바가 펴지며 각 아이콘에 대한 이름이 드러난다*. 
- 지도 화면 좌측 상단에는 **물놀이장, 바닥분수, 야외수영장을 선택할 수 있는 셀렉트바**가 있다. *해당 아이콘을 선택하면 지도 상에 해당 마커가 on/off 된다.*
- 지도 화면 우측 상단에는 **편의지수에 대한 간단한 범례**가 있다. **한 눈에 구분하기 쉽도록 편의지수의 등급에 따라 마커의 색깔을 3가지의 색깔로 다르게 해놓았는데**, 이것에 대해 페이지를 처음 접하는 유저도 손쉽게 알아볼 수 있도록 만들어주었다.  

### 공영주차장 마커를 클릭했을 때 

<img width="1680" alt="main2" src="https://github.com/liljw/ChildCarryMap/assets/129480514/04b595ec-da29-47fe-a0b4-6c350059bacb">

- 토글 버튼을 누르면 화면 좌측의 사이드 바가 펼쳐지는데, 그 중 공영주차장을 클릭하면, **사용자가 보고 있는 지도 비율 내의 모든 공영 주차장이 표시된다.** 
- 한번 더 누르면 off 되도록 만들었다. 

### 수유실 마커를 클릭했을 때

<img width="1680" alt="main3" src="https://github.com/liljw/ChildCarryMap/assets/129480514/41b16daf-690b-4225-b9fd-d0d3f546fcac">

- 마찬가지로 수유실 마커를 클릭했을 때, 사용자가 현재 보고 있는 지도 비율 내에 있는 모든 수유실의 위치가 마커와 함께 표시되는 것을 볼 수 있다.

### 물놀이장 마커를 클릭했을 때 나타나는 팝업 창

<img width="1680" alt="main4" src="https://github.com/liljw/ChildCarryMap/assets/129480514/d2ef2bc3-40aa-4c62-acd2-6f3c12dc42f6">

- **물놀이장 마커를 클릭하면, 작은 팝업창이 뜨며 해당 물놀이장에 대한 사진과 기본적인 정보, 그리고 창 하단에 상세페이지로 이동할 수 있는 버튼과 해당 물놀이장의 네이버 길찾기 페이지로 이동되는 하이퍼링크 버튼이 포함된 팝업 창이 뜬다.**
- 기본적인 정보에는 주소와 운영시간 혹은 기간, 그리고 전화번호가 적혀있다.

### 상세페이지 상단

<img width="1680" alt="detail1" src="https://github.com/liljw/ChildCarryMap/assets/129480514/a0a708bd-3464-4219-b8c7-e0ae5a6df1d9">

- 위의 팝업 창 하단의 상세페이지를 누르면 더 큰 상세페이지 팝업 창이 뜨게 된다. 
- 가장 상단에는 해당 물놀이장의 사진이, 그 아래 좌측에는 해당 물놀이장에 대한 더 세부적인 정보가 포함되어 있다. 
- **우측에는 편의지수와 리뷰 데이터로 도출한 긍/부정 비율이 긴 알약 형태로 시각화 되어있다.** 


### 상세페이지 하단
<img width="1680" alt="detail2" src="https://github.com/liljw/ChildCarryMap/assets/129480514/e7bcfd8c-f257-4712-a849-6be89ac42a54">

- 상세페이지를 아래로 스크롤 하게 되면 해당 물놀이장에 대한 더욱 세부적인 기능들이 포함되어있다.
- 좌측에는 **주변에 위치한 편의시설을 기준으로 상세 편의지수가 방사형 차트를 통해 시각화 되어있다.**
- 가운데에는 **해당 물놀이장과 해당 행정구역 내의 물놀이장들의 평균 편의지수와 비교하는 막대 그래프가 나타나있다.** 
- 우측에는 **리뷰 데이터를 기반으로 추출한 해당 물놀이장과 관련해 가장 많이 언급된 키워드들을 워드클라우드 형식으로 시각화 한 것이 나타나있다.**
-


---

## 기획

### 주제 선정 배경

<img width="1680" alt="why" src="https://github.com/liljw/ChildCarryMap/assets/129480514/346bb15a-9a4b-4ad3-a728-33521008bd17">

### 타겟

<img width="1680" alt="target" src="https://github.com/liljw/ChildCarryMap/assets/129480514/de16be7c-2ecd-4bf1-affc-f0ec5d661a29">

### 기대효과

<img width="1680" alt="expentance" src="https://github.com/liljw/ChildCarryMap/assets/129480514/54780fe3-26a8-4bbf-bb6b-9fa8673636bb">

---

# 데이터 분석

## 편의지수 개발

### 데이터 마트 구축 

<img width="1680" alt="datamart" src="https://github.com/liljw/ChildCarryMap/assets/129480514/7f6f0b0a-ed70-4439-8eb9-ba4d4bfda25a">

### 활용 데이터 셋

<img width="1680" alt="dataset" src="https://github.com/liljw/ChildCarryMap/assets/129480514/261b34f8-67a3-4722-8ff3-841364896323">

### 인덱스 도출 알고리즘

<img width="1680" alt="algorithm" src="https://github.com/liljw/ChildCarryMap/assets/129480514/04401f1e-f8ab-4954-b714-f74bcbb1bfdf">

### 만족거리 및 K값

<img width="1680" alt="K" src="https://github.com/liljw/ChildCarryMap/assets/129480514/bcc172fc-02fa-434f-8ae2-6268d6ec3542">

### 회귀 모형 및 예측

<img width="1680" alt="regression" src="https://github.com/liljw/ChildCarryMap/assets/129480514/285d6f9e-5081-41b7-8801-b15f49b0112c">

### 편의지수 도출 최종 모형

<img width="1680" alt="final model" src="https://github.com/liljw/ChildCarryMap/assets/129480514/899ff772-8455-4f83-90b4-cb9756e40371">

### 편의지수 범주화

<img width="1680" alt="binning" src="https://github.com/liljw/ChildCarryMap/assets/129480514/e3208f9a-d887-46ea-b706-5e2b452c8d54">

---

## 시각화 

### Folium

<img width="1680" alt="Folium" src="https://github.com/liljw/ChildCarryMap/assets/129480514/0bf98158-6cbc-4c97-a33a-180ed6467d54">

### 랭킹

<img width="1680" alt="Ranking" src="https://github.com/liljw/ChildCarryMap/assets/129480514/d3181f59-3180-4621-ac16-72f11cbbd9d7">

## 방사형 차트 (스파이더넷)

<img width="1680" alt="spidernet" src="https://github.com/liljw/ChildCarryMap/assets/129480514/c8673194-45a1-4b30-a0f7-5d2badb062d6">

---

# AI

## 긍/부정 감성분석

### 자연어처리

<img width="1680" alt="nlp" src="https://github.com/liljw/ChildCarryMap/assets/129480514/0a2d8e86-4b94-4853-953c-791050d94cce">

### 딥러닝 (LSTM)

<img width="1680" alt="lstm" src="https://github.com/liljw/ChildCarryMap/assets/129480514/0dc2374f-f723-49b9-8bcc-30d9f296a3af">

### 감성분석 결과 예시

<img width="1680" alt="example" src="https://github.com/liljw/ChildCarryMap/assets/129480514/f304b355-ff7f-4625-91fa-4c23e98b7eb2">

## 리뷰 키워드 추출

### 자연어처리 (워드클라우드)

<img width="1680" alt="wordcloud" src="https://github.com/liljw/ChildCarryMap/assets/129480514/fb9cac57-f1fa-46bf-8c95-5b176fa7fcb8">

---

# 클라우드

### 인프라 설계 구성도

<img width="1680" alt="cloud" src="https://github.com/liljw/ChildCarryMap/assets/129480514/639c583c-43c3-4437-9e0d-5145f2aa58a6">

### 데이터베이스 ERD

<img width="1680" alt="erd" src="https://github.com/liljw/ChildCarryMap/assets/129480514/9f87e416-ef0e-420e-ae00-7ae315743b46">

---

## 확장가능성

<img width="1680" alt="availability" src="https://github.com/liljw/ChildCarryMap/assets/129480514/aa71d7db-d5f1-46a7-8e32-b457090e2b95">

---
