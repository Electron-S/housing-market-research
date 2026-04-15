# Housing Market Research

재개발·재건축 사업지 시장조사 및 적정분양가 검토를 위한 리서치 워크스페이스다. [KCS-AI](https://github.com/gaebalai/KCS-AI) 건설경영 제안서 파이프라인을 기반으로, 한국 부동산 분양 시장에 특화된 15단계 분석·집필 파이프라인으로 재구성했다.

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
2. 산출물 유형에 맞는 템플릿을 고른다.
3. `04_workspace/[target_id]_[agent]_KR/` 또는 `04_workspace/[target_id]_KR/` 폴더를 만든다.
4. 각 STEP 절차서는 해당 STEP 착수 직전에만 읽는다.

## 디렉터리 구조

```text
housing-market-research/
├── 00_ref/                          # 프로젝트 개요·전략
├── 01_data/                         # 원천 데이터
├── 02_plan/                         # 워크플로우·절차서·템플릿
│   ├── 주택시장조사_마스터_워크플로우.md  ← 항상 먼저 읽기
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
└── 05_output/                         # 레거시 최종 DOCX 보관 경로
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
| 15 | 최종화 | `report_designed_[agent].docx` |

## 환경 설정

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

외부 API를 직접 호출하는 확장 스크립트를 쓸 때만 `.env` 파일을 사용한다 (`.env.example` 참고):

```
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
GEMINI_API_KEY=...
```

설치 후 빠른 검증:

```bash
python3 -c "from docx import Document; print('python-docx OK')"
python3 03_code/md_to_docx_converter.py seongsu-residential_codex_KR
python3 03_code/improve_docx_design.py 04_workspace/seongsu-residential_codex_KR/report_draft_codex.docx
python3 03_code/count_docx_chars.py 04_workspace/seongsu-residential_codex_KR/report_designed_codex.docx
```

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
- `04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx`
- `04_workspace/[target_id]_[agent]_KR/STEP12_review_packet_[agent].md`
- `04_workspace/[target_id]_[agent]_KR/STEP12_output_[agent].md`

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
- [02_plan/부동산_분석_워크플로우.md](02_plan/부동산_분석_워크플로우.md)
