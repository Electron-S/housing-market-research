# Housing Market Research

재개발·재건축 사업지 시장조사 및 적정분양가 검토를 위한 리서치 워크스페이스다.
STEP0~STEP15의 16단계 분석·집필 파이프라인으로 운영한다.
기본 사용자는 GS건설 실무 담당자를 상정하며, 보고서에는 경쟁사 비교분석과 GS건설 대응 시사점을 포함한다.

## 산출물

| 유형 | 설명 |
|---|---|
| **아파트 시장조사 보고서** | 재개발·재건축 사업지 사업성 검토 및 적정분양가 산정 (주력) |
| **상가 시장조사 보고서** | 근린생활시설 사업성 검토 및 층별 적정분양가 산정 (주력) |
| 권역 시장 브리프 | 권역별 가격·거래·청약 동향 요약 (보조) |
| 사업지 입지 분석 | 교통·학군·인프라·개발계획 분석 (보조) |
| 경쟁 단지 비교 | 비교 단지 선정·가격·분양률 비교 (보조) |

## 빠른 시작

```bash
# 1. 가상환경 생성 (최초 1회)
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# 2. Claude Code 실행 후 사업구역과 보고서 유형 지시
# 예: "하남 리젠하임 아파트 시장조사 진행해줘"
```

> **모든 Python 스크립트는 `.venv/bin/python`으로 직접 호출한다. `python` 또는 `python3` 단독 명령은 동작하지 않는다.**

## 16단계 워크플로우

| STEP | 이름 | 산출물 |
|---|---|---|
| 0 | 사업 현황 사전 조사 | `STEP0_output.md` |
| 1 | 의뢰 정의 | `STEP1_output.md` |
| 2 | 거시·정책 환경 | `STEP2_output.md` |
| 3 | 가격·거래 추이 | `STEP3_output.md` |
| 4 | 수요 분석 | `STEP4_output.md` |
| 5 | 공급 분석 | `STEP5_output.md` |
| 6 | 입지 분석 | `STEP6_output.md` |
| 7 | 경쟁 비교 | `STEP7_output.md` |
| 8 | 리스크 정리 | `STEP8_output.md` |
| 9 | 결론 및 시사점 | `STEP9_output.md` |
| 10 | 보고서 집필 준비 | `STEP10_output.md` |
| 11 | 보고서 집필 | `STEP11_[유형]_draft.md` |
| 12 | 품질 리뷰 (MD) | `STEP12_output_[agent].md` |
| 13 | MD→DOCX 변환 | `report_designed_[agent].docx` |
| 14 | 품질 리뷰 (DOCX) | `STEP14_output.md` |
| 15 | 최종화 | `05_output/[target_id]_designed.docx` |

**STEP12 품질 리뷰 원칙**: 실행 중인 에이전트(Claude 또는 Codex)가 보고서를 직접 5개 기준으로 평가하고 최대 3회 반복한다. 에이전트별 결과는 별도 파일로 누적돼 추후 품질 비교에 활용된다.

## 디렉터리 구조

```text
housing-market-research/
├── 00_ref/                              # 프로젝트 개요·전략
├── 01_data/[target_id]/                 # 사업지별 원본 데이터 저장소
├── 02_plan/                             # 워크플로우·절차서·템플릿
│   ├── 주택시장조사_마스터_워크플로우.md
│   ├── 아파트시장조사_워크플로우.md
│   ├── 상가시장조사_워크플로우.md
│   ├── STEP0_절차서.md ~ STEP15_절차서.md
│   └── 템플릿_*.md
├── 03_code/                             # Python 유틸
├── 04_workspace/[target_id]_[agent]_KR/
│   ├── STEP0_output.md ~ STEP10_output.md
│   ├── STEP11_[유형]_draft.md
│   ├── STEP12_review_packet_[agent].md
│   ├── STEP12_output_[agent].md
│   ├── STEP14_output.md
│   ├── report_draft_[agent].docx
│   ├── report_designed_[agent].docx
│   └── images/
└── 05_output/                           # 최종 DOCX 보관
```

## 주요 스크립트

| 스크립트 | 용도 | STEP |
|---|---|---|
| `multi_model_evaluate.py` | 품질 리뷰 패킷 생성 + Iteration 누적 | 12 |
| `md_to_docx_converter.py` | Markdown → Word 변환 | 13 |
| `improve_docx_design.py` | 폰트·표·여백 디자인 보정 + `05_output/` 배치 | 13 |
| `count_docx_chars.py` | DOCX 문자수 확인 (목표 8,000~12,000자) | 13, 14 |
| `count_chars.py` | Markdown 문자수 예비 확인 | 11 |
| `analyze_docx.py` | DOCX 구조 분석 | 14 |
| `insert_images.py` | DOCX 이미지 플레이스홀더 삽입 | 13 |

### STEP13 변환 전체 실행 순서

```bash
# STEP13: MD → DOCX
.venv/bin/python 03_code/md_to_docx_converter.py [target_id]_[agent]_KR \
  --input STEP11_아파트보고서_draft.md

# STEP13: 디자인 보정
.venv/bin/python 03_code/improve_docx_design.py \
  04_workspace/[target_id]_[agent]_KR/report_draft_[agent].docx \
  04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx

# STEP13: 문자수 검증
.venv/bin/python 03_code/count_docx_chars.py \
  04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx
```

### STEP12 품질 리뷰 실행

```bash
# 폴더명에 에이전트 태그(_claude_KR / _codex_KR)가 있으면 자동 감지
.venv/bin/python 03_code/multi_model_evaluate.py [target_id]_[agent]_KR

# 태그가 없을 경우 명시
.venv/bin/python 03_code/multi_model_evaluate.py [target_id]_KR --reviewer claude
```

## 상가 시장조사 추가 원칙

- `STEP3`: 층별 임대료·공실·1층 프리미엄이 핵심 입력값이다.
- `STEP7`: 비교 사례별 층별 평단가·임대료·수익률 비교표를 남긴다.
- `STEP9`: `1층 핵심 / 1층 비핵심 / 비1층 목적형 / 비1층 일반형` 기준 권고 평단가 밴드를 표로 제시한다. 정성 표현만으로 종료 금지.
- `STEP11`: 최종 보고서 본문에 STEP9 가격표가 실제로 들어갔는지 확인한다.

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

- [02_plan/주택시장조사_마스터_워크플로우.md](02_plan/주택시장조사_마스터_워크플로우.md)
- [02_plan/아파트시장조사_워크플로우.md](02_plan/아파트시장조사_워크플로우.md)
- [02_plan/상가시장조사_워크플로우.md](02_plan/상가시장조사_워크플로우.md)
- [00_ref/부동산_분석_프로젝트_개요.md](00_ref/부동산_분석_프로젝트_개요.md)
- [00_ref/부동산_분석_프로젝트_전략.md](00_ref/부동산_분석_프로젝트_전략.md)
