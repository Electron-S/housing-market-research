# 01_data

원천 데이터 보관 폴더다.
실제 운영에서는 사업구역별 원본 수집함으로 사용한다.

## 원칙

- `01_data`에는 원본 또는 원본에 준하는 수집본만 둔다.
- 가공, 해석, 요약, 표 재작성은 `04_workspace/`에서 한다.
- 원본 파일은 가능하면 수정하지 않는다.
- 출처와 기준 시점을 파일명 또는 같은 폴더의 메모에 남긴다.

## 권장 구조

```text
01_data/
└── [target_id]/
    ├── 01_gs_project/
    ├── 02_policy_macro/
    ├── 03_price_trade/
    ├── 04_demand/
    ├── 05_supply_location/
    ├── 06_competitors/
    └── 99_notes/
```

## 폴더 용도

- `01_gs_project`: 사업구역 관련 GS건설 사업 내용, 보도자료, 분양/시공/정비사업 관련 기사, 정비사업 공고문
- `02_policy_macro`: 금리, 대출규제, 세제, 공급정책 자료 원문
- `03_price_trade`: 실거래가 CSV, 시세 표, 거래량 캡처, 청약 결과 원본
- `04_demand`: 인구, 가구, 소득, 고용, 전입전출 통계 원본
- `05_supply_location`: 입주물량, 개발계획, 교통, 학군, 생활인프라 자료 원본
- `06_competitors`: 경쟁 단지 분양가, 실거래가, 상품 비교 자료 원본
- `99_notes`: 수집 로그, 출처 목록, 기준 시점 메모

## 파일명 규칙

```text
[yyyymmdd]_[source]_[topic]_[asof].ext
```

예시:

- `20260415_molit_realtrade_seongsu_202603.csv`
- `20260415_rone_priceindex_seongdong_202604.xlsx`
- `20260415_news_gs_project_cheongnyangni_20260415.md`
- `20260415_kosis_population_seongdong_2025.xlsx`

## 운영 방식

1. STEP1 시작 시 `01_data/[target_id]/01_gs_project/`에 GS건설 사업 관련 원본을 먼저 모은다.
2. STEP2~7 진행 중 수집한 원본은 해당 하위 폴더에 저장한다.
3. `04_workspace/[target_id]_KR/`에서는 이 원본을 근거로 표와 해석을 작성한다.
4. 보고서에는 원본 파일 자체를 복붙하지 말고, 정리된 수치와 출처만 사용한다.
