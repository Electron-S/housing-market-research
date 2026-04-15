# Housing Market Research

재개발·재건축 사업지 시장조사 및 적정분양가 검토를 위한 리서치 워크스페이스다. 한국 부동산 분양 시장에 특화된 15단계 분석·집필 파이프라인으로 재구성했다. 기본 사용자는 GS건설 실무 담당자를 상정하며, 보고서에는 GS건설 입장에서의 경쟁사 비교분석과 대응 시사점을 포함한다. 사업구역이 특정되면 해당 구역에서 GS건설이 추진 중이거나 검토 중인 사업 내용을 먼저 확인한 뒤 본 분석에 들어간다.

## 산출물

| 유형 | 설명 |
|---|---|
| 아파트 시장조사 보고서 | 재개발·재건축 사업지 적정분양가 검토 |
| 상가 시장조사 보고서 | 근린생활시설 적정분양가 검토 |
| 권역 시장 브리프 | 권역별 가격·거래·청약 동향 요약 |
| 사업지 입지 분석 | 교통·학군·인프라·개발계획 분석 |
| 경쟁 단지 비교 | 비교 단지 선정·가격·분양률 비교 |

## 시작 순서

1. [`02_plan/주택시장조사_마스터_워크플로우.md`](02_plan/주택시장조사_마스터_워크플로우.md)를 읽는다.
2. 보고서 유형이 `아파트 시장조사 보고서`면 [`02_plan/아파트시장조사_워크플로우.md`](02_plan/아파트시장조사_워크플로우.md)를, `상가 시장조사 보고서`면 [`02_plan/상가시장조사_워크플로우.md`](02_plan/상가시장조사_워크플로우.md)를 읽는다.
3. 사용자가 `사업구역에 대해 아파트 시장조사 STEP1부터 진행해` 또는 `사업구역에 대해 상가 시장조사 STEP1부터 진행해`라고 지시하면 해당 유형으로 STEP1부터 시작한다.
4. 사업구역이 주어지면 해당 구역의 GS건설 사업 내용을 먼저 인터넷 검색으로 확인한다.
5. 산출물 유형에 맞는 템플릿을 고른다.
6. `04_workspace/[target_id]_[agent]_KR/` 또는 `04_workspace/[target_id]_KR/` 폴더를 만든다.
7. 각 STEP 절차서는 해당 STEP 착수 직전에만 읽는다.

상가 시장조사 추가 원칙:

- 상가는 `STEP3 -> STEP7 -> STEP9 -> STEP10/11`로 이어지는 `평단가 산정 체인`이 끊기면 안 된다.
- `STEP3`에서는 `층별 임대료`, `공실`, `서울 평균 대비 위치`를 잡는다.
- `STEP7`에서는 비교 사례별 `층별 평단가`, `임대료`, `수익률`을 정리한다.
- `STEP9`에서는 정성 표현만 쓰지 말고 `1층 핵심 / 1층 비핵심 / 비1층 목적형 / 비1층 일반형` 기준 `권고 평단가 밴드`를 표로 제시한다.
- `STEP10`과 `STEP11` 최종 보고서에는 STEP9의 `층별 적정 평단가 밴드 표`를 그대로 승계한다.
- 설계가 미확정이어도 숫자를 비워두지 말고 `가정 기반 예비 밴드`를 작성한다.

## 디렉터리 구조

```text
housing-market-research/
├── 00_ref/                          # 프로젝트 개요·전략
├── 01_data/                         # 사업지별 원본 데이터 저장소
├── 02_plan/                         # 워크플로우·절차서·템플릿
│   ├── 주택시장조사_마스터_워크플로우.md  ← 항상 먼저 읽기
│   ├── 아파트시장조사_워크플로우.md
│   ├── 상가시장조사_워크플로우.md
│   ├── STEP1_절차서.md ~ STEP10_절차서.md
│   └── 템플릿_*.md
├── 03_code/                         # Python 유틸
├── 04_workspace/
│   ├── 공통_KR/                     # 주택시장 공통 KB (STEP0 수행 후 생성)
│   └── [target_id]_[agent]_KR/     # 사업지별 작업공간 (예: _claude, _codex)
│       ├── STEP1_output.md ~ STEP10_output.md
│       ├── STEP11_[유형]_draft.md
│       ├── STEP12_review_packet_[agent].md
│       ├── STEP12_output_[agent].md
│       ├── report_draft_[agent].docx
│       ├── report_designed_[agent].docx
│       └── images/
└── 05_output/                         # 최종 DOCX 보관 경로
```

## 15단계 워크플로우

| STEP | 이름 | 산출물 |
|---|---|---|
| 0 | 주택시장 공통정보 수집 (사전 1회) | `공통_KR/*.md` |
| 1 | 사업지 선정·기본정보 | `STEP1_output.md` |
| 2 | 사업 개요 분석 | `STEP2_output.md` |
| 3 | 거시·정책 환경 | `STEP3_output.md` |
| 4 | 지역 시장 환경 | `STEP4_output.md` |
| 5 | 입지 분석 | `STEP5_output.md` |
| 6 | 비교 단지 분석 | `STEP6_output.md` |
| 7 | 수급 구조화 | `STEP7_output.md` |
| 8 | 분양가 산정 | `STEP8_output.md` |
| 9 | 분양성 평가·리스크 | `STEP9_output.md` |
| 10 | 보고서 장구성 설계 | `STEP10_output.md` |
| 11 | 보고서 집필 | `STEP11_[유형]_draft.md` |
| 12 | 품질 리뷰 (MD) | 에이전트 직접 평가 → 미달 시 수정 반복 |
| 13 | MD→DOCX 변환 | `report_draft_[agent].docx` |
| 14 | 품질 리뷰 (DOCX) | 서식·데이터·가독성 점검 |
| 15 | 최종화 | `05_output/*.docx` |

상가 시장조사에서 특히 다시 확인할 STEP:

- `STEP3`: 상가는 `매매가 추이`만이 아니라 `층별 임대료`, `공실`, `1층 프리미엄`이 핵심 입력값이다.
- `STEP7`: 상가는 유사 사례별 `임대료·수익률·층별 가격` 비교표를 남겨야 한다.
- `STEP9`: 상가는 `공격적/보수적` 같은 문장만으로 종료하면 안 되고 `층별 적정 평단가 밴드`를 반드시 적어야 한다.
- `STEP10~11`: 최종 보고서 본문에 STEP9 가격표가 실제로 들어갔는지 확인한다.

## 환경 설정

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

설치 후 빠른 검증:

```bash
python3 -c "from docx import Document; print('python-docx OK')"
python3 03_code/md_to_docx_converter.py seongsu-residential_codex_KR
python3 03_code/improve_docx_design.py 04_workspace/seongsu-residential_codex_KR/report_draft_codex.docx
python3 03_code/count_docx_chars.py 04_workspace/seongsu-residential_codex_KR/report_designed_codex.docx
```

스크립트 실행 원칙:

- 프로젝트 스크립트는 `venv` 또는 `.venv` 가상환경에서 실행한다.
- `STEP11_보고서_draft.md`가 없더라도 `STEP11_상가보고서_draft.md`, `STEP11_아파트보고서_draft.md` 같은 유형별 파일명을 자동 탐색하도록 스크립트를 맞춘다.

## 주요 스크립트

| 스크립트 | 용도 | 사용 STEP |
|---|---|---|
| `md_to_docx_converter.py` | Markdown → Word 변환 | 13 |
| `insert_images.py` | DOCX에 이미지 삽입 | 13 |
| `improve_docx_design.py` | 폰트·표·여백 디자인 보정 | 13 |
| `count_docx_chars.py` | DOCX 문자수 확인 | 13, 14 |
| `count_chars.py` | Markdown 문자수 확인 | 11, 12 |
| `analyze_docx.py` | DOCX 구조 분석 | 14 |
| `multi_model_evaluate.py` | STEP12 리뷰 패킷 생성 및 반복 리뷰 준비 | 12 |

```bash
# 실행 예시
python 03_code/md_to_docx_converter.py seongsu-residential_codex_KR \
  --title "성수 주거지역 시장조사 보고서"

python 03_code/multi_model_evaluate.py seongsu-residential_codex_KR --reviewer codex
```

기본 산출물 경로:

- `04_workspace/[target_id]_[agent]_KR/report_draft_[agent].docx`
- `05_output/[target_id]_[agent]_designed.docx` 또는 이에 준하는 최종본
- `04_workspace/[target_id]_[agent]_KR/STEP12_review_packet_[agent].md`
- `04_workspace/[target_id]_[agent]_KR/STEP12_output_[agent].md`

운영 원칙:

- 기본 보고서 유형은 `아파트 시장조사 보고서`, `상가 시장조사 보고서`다.
- 적정 분양가 제안은 근거가 허용하는 범위에서 약간 공격적으로 설정한다.
- 상가 보고서의 적정 분양가 제안은 `층별·위치별 평단가 밴드` 기준으로 작성한다.
- 상가 보고서에서 숫자 없는 `약간 공격적`, `보수적` 같은 정성 문구만 남기고 종료하지 않는다.
- 최종 DOCX는 `05_output`에 둔다.
- 원본 수집 자료는 `01_data/[target_id]/`에 저장하고, 가공 결과는 `04_workspace/[target_id]_KR/`에서 작성한다.

## 주요 데이터 소스

- 국토교통부 실거래가 공개시스템
- 한국부동산원 R-ONE
- KB부동산
- 청약홈 (청약 경쟁률·당첨가점)
- KOSIS 국가통계포털
- 한국은행 ECOS
- 서울열린데이터광장
- 지자체 도시계획·정비사업 공개자료

## 핵심 문서

- [00_ref/부동산_분석_프로젝트_개요.md](00_ref/부동산_분석_프로젝트_개요.md)
- [00_ref/부동산_분석_프로젝트_전략.md](00_ref/부동산_분석_프로젝트_전략.md)
- [02_plan/주택시장조사_마스터_워크플로우.md](02_plan/주택시장조사_마스터_워크플로우.md)
- [02_plan/아파트시장조사_워크플로우.md](02_plan/아파트시장조사_워크플로우.md)
- [02_plan/상가시장조사_워크플로우.md](02_plan/상가시장조사_워크플로우.md)
- [02_plan/부동산_분석_워크플로우.md](02_plan/부동산_분석_워크플로우.md)
