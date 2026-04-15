# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

주택사업 실무자용 **재개발·재건축 사업지 시장조사** 워크스페이스다. KCS-AI(건설경영 제안서 파이프라인)를 기반으로, 한국 부동산 분양 시장에 특화된 15단계 분석·집필 파이프라인으로 재구성했다.

**최종 산출물**:
- 아파트 시장조사 보고서 (적정분양가 검토)
- 상가 시장조사 보고서 (근린생활시설 적정분양가 검토)

## Mandatory Rules

보고서 작성 지시 시:

1. **마스터 워크플로우 먼저 읽기**: [`02_plan/주택시장조사_마스터_워크플로우.md`](02_plan/주택시장조사_마스터_워크플로우.md)를 가장 먼저 읽어 전체 플로우와 산출물 유형을 파악한다.

2. **STEP 절차서는 just-in-time으로 읽기**: 각 `02_plan/STEPx_절차서.md`는 해당 STEP 착수 **직전**에만 읽는다. 미리 전체 로딩 금지 (컨텍스트 낭비).
   - 올바름: STEP3 시작 → `STEP3_절차서.md` 읽기 → 실행 → STEP4 시작 → `STEP4_절차서.md` 읽기
   - 잘못됨: STEP1~10 절차서 전체 로딩 후 실행

3. **산출물 유형 확인**: 아파트 보고서 / 상가 보고서 / 권역 브리프 / 사업지 분석 / 경쟁 단지 비교 중 무엇인지 먼저 특정한다.

## Working Rules

1. 모든 수치에는 기준 시점과 출처를 적는다.
2. 사실, 해석, 판단을 섞지 않는다.
3. 결론은 행동 문장으로 쓴다.
4. 확실하지 않은 내용은 추정이라고 적는다.
5. 출처 인용 필수 (국토부 실거래가 시스템, KB, R-ONE 등 특정 URL 또는 자료명).

## Writing Rules

- 광고 문구처럼 쓰지 않는다
- 입지 설명은 반드시 수요와 연결한다
- 비교 단지 선정 근거를 적는다
- 정책 변수와 공급 리스크를 빠뜨리지 않는다

## Directory Structure

```
housing-market-research/
├── 00_ref/                              # 프로젝트 개요·전략
│   ├── 부동산_분석_프로젝트_개요.md
│   └── 부동산_분석_프로젝트_전략.md
├── 01_data/                             # 원시 데이터
├── 02_plan/                             # 작업 절차서
│   ├── 주택시장조사_마스터_워크플로우.md    # ← 마스터 (항상 먼저 읽기)
│   ├── 부동산_분석_워크플로우.md           # 10단계 흐름 요약
│   ├── STEP1_절차서.md ~ STEP10_절차서.md  # STEP별 상세 절차
│   ├── 템플릿_경쟁단지비교.md
│   ├── 템플릿_권역시장브리프.md
│   └── 템플릿_사업지입지분석.md
├── 03_code/                             # Python 스크립트
├── 04_workspace/
│   ├── 공통_KR/                         # 주택시장 공통 KB (사전 1회 수집)
│   │   ├── 거시환경_금리정책.md
│   │   ├── 권역별시장동향.md
│   │   └── 분양시장동향.md
│   └── [target_id]_KR/                 # 사업지별 작업공간
│       ├── STEP1_output.md ~ STEP10_output.md
│       ├── STEP11_[유형]_draft.md
│       └── images/
└── 05_output/                  # 최종 DOCX
    └── [target_id].docx
```

> `공통_KR/` 폴더는 STEP0 수행 후 생성된다. 아직 없으면 STEP0부터 시작한다.

## Typical Flow (15단계 + STEP0 사전준비)

| STEP | 이름 | 비고 |
|---|---|---|
| **0** | **주택시장 공통정보 수집** (사전 1회) | 거시환경·정책·시장 기반자료 — `공통_KR/*.md` |
| 1 | 사업지 선정·기본정보 확인 | 사업명·위치·시행사·인허가 현황 |
| 2 | 사업 개요 분석 | 타입별 세대수·평면·배치 구성 |
| 3 | 거시·정책 환경 | 금리·DSR·분양가상한제·재건축 규제 |
| 4 | 지역 시장 환경 | 권역 가격·거래·청약 동향 |
| 5 | 입지 분석 | 교통·학군·인프라·주변 개발계획 |
| 6 | 비교 단지 분석 | 선정 근거·가격·분양률·상품 비교 |
| 7 | 수급 구조화 | 공급 물량·수요층·미분양 리스크 |
| 8 | 분양가 산정 | 기준가·차등 지수 적용·타입별 도출 |
| 9 | 분양성 평가·리스크 정리 | 청약 흡수력·분양 속도·리스크 |
| 10 | 보고서 장구성 설계 | 섹션 구성·표지 정보 확정 |
| 11 | 보고서 집필 | `STEP11_[유형]_draft.md` |
| 12 | 품질 리뷰·개선 루프 (MD) | 5기준 AI 평가 → A 미달 수정 → 반복 (최대 5회) |
| 13 | MD→DOCX 변환 | 변환·이미지 삽입·디자인 보정 |
| 14 | 품질 리뷰 (DOCX) | 서식·데이터·가독성 점검 |
| 15 | 최종화 | 최종본 확정 및 기록 |

### 산출물 유형별 필수/선택 STEP

| 산출물 유형 | 필수 STEP | 선택 STEP | 사용 템플릿 |
|---|---|---|---|
| 아파트·상가 분양가 보고서 | 0~11 전체 | — | `STEP11_[유형]_draft.md` |
| 권역 시장 브리프 | 1·2·3·4·5·9·10 | 6·7·8 | `템플릿_권역시장브리프.md` |
| 사업지 입지 분석 | 1·2·4·5·6·7·8·9·10 | 3 | `템플릿_사업지입지분석.md` |
| 경쟁 단지 비교 | 1·3·6·7·9·10 | 2·4·5·8 | `템플릿_경쟁단지비교.md` |

## File Conventions

- 작업 폴더: `04_workspace/[target_id]_KR/`
- 중간 산출물: `STEP1_output.md` ~ `STEP10_output.md`
- 집필 파일: `STEP11_[유형]_draft.md` (예: `STEP11_아파트보고서_draft.md`)
- 이미지 폴더: `04_workspace/[target_id]_KR/images/`
- 최종 보고서: `05_output/[target_id].docx`

## Common Commands

### 환경 설정
```bash
# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### Python 실행 규칙 (중요)
**모든 Python 스크립트는 가상환경 내에서 실행.** 각 명령 전에 venv 활성화.

### 스크립트 실행 예시
```bash
# MD → DOCX 변환 (STEP13)
python 03_code/md_to_docx_converter.py seongsu-residential_KR \
  --title "성수 주거지역 시장조사 보고서"

# 이미지 삽입 (STEP13)
python 03_code/insert_images.py \
  04_workspace/seongsu-residential_KR/STEP11_아파트보고서_draft.docx \
  05_output/seongsu-residential.docx

# 디자인 개선 (STEP13)
python 03_code/improve_docx_design.py 05_output/seongsu-residential.docx

# 문자수 확인 (STEP13/14)
python 03_code/count_docx_chars.py 05_output/seongsu-residential_designed.docx

# MD 파일 문자수 확인 (집필 중)
python 03_code/count_chars.py 04_workspace/seongsu-residential_KR/STEP11_아파트보고서_draft.md

# DOCX 구조 분석
python 03_code/analyze_docx.py 05_output/seongsu-residential_designed.docx

# STEP12 멀티모델 AI 평가
python 03_code/multi_model_evaluate.py seongsu-residential_KR
```

## Code Architecture

### 03_code/ 스크립트

#### md_to_docx_converter.py
- `--lang ko` 자동 추정 (`_KR` 접미사로 ko)
- `--title`, `--date` override 가능
- 한국어 프리셋: 폰트(맑은고딕), 행간(1.15), 여백(25mm) 자동 적용

#### insert_images.py
- 한국어 플레이스홀더 `(※그림1은 별도 이미지로 삽입)` 자동 검출
- `_KR` 접미사 폴더 자동 탐색

#### improve_docx_design.py
- 폰트·표·여백 디자인 보정. 출력에 `_designed` 접미사 붙음.

#### count_docx_chars.py
- DOCX 문자수 확인 (공백 포함). 한국어 기준 8,000~12,000자 검증용.

#### count_chars.py
- Markdown 파일 문자수 확인. 집필 중 분량 체크용.

#### analyze_docx.py
- DOCX 구조 분석 (단락수, 표수, 스타일 사용 현황).

#### multi_model_evaluate.py
- STEP12 멀티모델 AI 평가. 5기준 A등급까지 반복 평가.
- `.env` 파일에 `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY` 필요.

## Evaluation Criteria (STEP12)

STEP12에서 5개 기준으로 A/B/C 평가:

| 기준 | 고평가 조건 |
|---|---|
| 데이터 신뢰성 | 비교 단지 가격·거래 데이터에 출처(국토부·KB·R-ONE)와 기준 시점 명시 |
| 입지 분석 | 교통·학군·인프라가 타깃 수요층과 구체적으로 연결 |
| 비교 단지 적정성 | 비교 단지 선정 근거 타당, 가격 차등 지수 적용 근거 명확 |
| 분양가 산정 근거 | 지수 적용 방법론과 결과값이 논리적으로 연결 |
| 결론 실효성 | 분양가와 분양성 판단(청약경쟁률, 흡수 속도)이 실행 가능한 수준으로 제시 |

## Data Sources

| 출처 | 용도 |
|---|---|
| 국토교통부 실거래가 공개시스템 (rt.molit.go.kr) | 아파트 매매·전세 실거래가 |
| 한국부동산원 R-ONE (r-one.co.kr) | 가격지수, 거래량, 청약통계 |
| KB부동산 (kbland.kr) | 시세, 매물, KB주택가격지수 |
| 청약홈 (applyhome.co.kr) | 청약 경쟁률, 당첨가점 |
| KOSIS 국가통계포털 | 인구·가구·주택 통계 |
| 한국은행 ECOS (ecos.bok.or.kr) | 금리, 대출 통계 |
| 서울열린데이터광장 (data.seoul.go.kr) | 서울 도시계획·정비사업 자료 |
| 지자체 도시계획·정비사업 공개자료 | 개발계획, 사업인가 현황 |

## Document Specification

- 형식: Word (.docx)
- 페이지: A4, 10~15페이지 (보고서 유형에 따라 상이)
- 문자수: **한국어 기준 8,000~12,000자 (공백 포함)**
  - 확인: `python 03_code/count_docx_chars.py <path>`
- 폰트: 맑은고딕 12pt
- 행간: 1.15
- 여백: 25mm

## Notes for AI Agents

- 모든 중간 산출물은 마크다운으로 `04_workspace/[target_id]_KR/STEPx_output.md`에 저장
- 구조적 사고 적용: 데이터 수집 → 시장 분석 → 분양가 산정 → 분양성 평가 → 평가기준 검증
- 출처 인용 필수 (국토부 실거래가 시스템, KB, R-ONE 등 특정 URL 또는 자료명과 기준 시점)
- 추상적 시장 설명이 아닌 구체적·실행 가능한 분양가 및 분양성 판단에 집중
- 데이터 없이 단정하지 말고, 추정임을 명시한 후 근거를 제시
