# CLAUDE.md

This file is the operating guide for Claude Code in this repository.

## What Claude Should Do

- 사람용 개요나 실행 예시가 필요하면 [`README.md`](README.md)를 본다.
- 실제 작업 절차의 정본은 [`02_plan/주택시장조사_마스터_워크플로우.md`](02_plan/주택시장조사_마스터_워크플로우.md)다.
- Claude는 이 문서를 "행동 규칙"으로 사용하고, 프로젝트 설명은 반복하지 않는다.
- 기본 보고서 유형은 `아파트 시장조사 보고서`와 `상가 시장조사 보고서` 두 가지다.

## Required Reading Order

보고서 작성 또는 STEP 진행 요청을 받으면 아래 순서를 지킨다.

1. [`02_plan/주택시장조사_마스터_워크플로우.md`](02_plan/주택시장조사_마스터_워크플로우.md)를 먼저 읽어 산출물 유형과 전체 플로우를 파악한다.
2. 현재 요청이 어떤 산출물인지 특정한다.
3. 아파트 시장조사면 [`02_plan/아파트시장조사_워크플로우.md`](02_plan/아파트시장조사_워크플로우.md), 상가 시장조사면 [`02_plan/상가시장조사_워크플로우.md`](02_plan/상가시장조사_워크플로우.md)를 읽는다.
4. 필요한 STEP에 들어가기 직전에 해당 `02_plan/STEPx_절차서.md`만 읽는다.
5. **STEP0은 모든 보고서 작성 전 필수 선행 단계다.** `STEP0_output.md`가 없으면 STEP0(사업 현황 사전 조사)부터 시작한다.
6. 사용자가 `STEP1부터 진행해`처럼 지시해도, `STEP0_output.md`가 없으면 STEP0부터 시작한다. STEP0 결과가 있으면 STEP1부터 진행해도 된다.
7. **전체 워크플로우는 STEP0~STEP15 (16단계)다.** STEP11(집필) → STEP12(MD 품질 리뷰) → STEP13(DOCX 변환) → STEP14(DOCX 품질 리뷰) → STEP15(최종화) 순서를 반드시 지킨다.

금지:

- 절차서를 한 번에 미리 읽기
- 출처와 기준 시점 없이 수치 단정하기
- 근거 없이 분양가나 분양성 결론 내리기
- **STEP12 품질 리뷰를 건너뛰고 DOCX 변환으로 넘어가기**
- **STEP14 DOCX 품질 리뷰를 건너뛰고 최종화하기**

## Output Rules

- 원본 수집 자료는 `01_data/[target_id]/`에 저장하고, 가공·집필 산출물은 `04_workspace/[target_id]_[agent]_KR/`에 저장한다.
- 작업 폴더는 `04_workspace/[target_id]_[agent]_KR/`를 기본으로 사용한다.
- 중간 산출물은 `STEP1_output.md`부터 `STEP10_output.md`까지 저장한다.
- 집필 파일은 `STEP11_[유형]_draft.md` 형식을 사용한다.
- 리뷰 패킷은 `STEP12_review_packet_[agent].md`, 리뷰 결과는 `STEP12_output_[agent].md`를 사용한다.
- DOCX 초안은 `report_draft_[agent].docx`를 작업 폴더에 저장한다.
- 최종 DOCX는 `05_output/`에 저장하고, 파일명은 기본적으로 `report_designed_[agent].docx` 또는 대상 ID 기반 최종본으로 관리한다.
- `[agent]` 자리는 현재 실행 에이전트 이름을 사용한다. Claude Code에서 작업하면 `claude`, Codex에서 작업하면 `codex`를 사용한다.

## Analysis Rules

1. 모든 수치에는 기준 시점과 출처를 적는다.
2. 사실, 해석, 판단을 분리해서 쓴다.
3. 확실하지 않은 내용은 추정이라고 명시한다.
4. 비교 단지 선정 근거를 반드시 적는다.
5. 입지 설명은 교통, 학군, 인프라를 수요층과 연결해서 쓴다.
6. 정책 변수와 공급 리스크를 빠뜨리지 않는다.
7. GS건설 관점에서 경쟁사 브랜드, 상품, 가격, 분양 성과를 비교하고 대응 포인트를 정리한다.
8. STEP0에서 확인한 GS건설 포지션(수주 전/후)에 따라 보고서 목적을 분기한다. 수주 전이면 제안 전략 수립이 목적이고, 수주 후이면 분양·임대 전략 수립이 목적이다. 사업구역 관련 GS건설 사업 내용은 STEP0에서 인터넷 검색으로 먼저 확인하고, 확인된 사실과 추정 내용을 분리해 `STEP0_output.md`에 기록한다.
9. STEP별로 수집한 원본 자료는 가능한 한 `01_data/[target_id]/`에 먼저 저장하고, 작업 공간에는 가공 결과만 남긴다.
10. 적정 분양가 제안은 보수적으로 깎지 말고, 근거가 유지되는 범위에서 약간 공격적으로 설정한다.
11. 결론은 실행 가능한 문장으로 쓴다.

## Writing Rules

- 광고 문구처럼 쓰지 않는다.
- 추상적 시장 설명보다 가격, 수요, 공급, 흡수 가능성 판단을 우선한다.
- 경쟁 비교가 들어가는 보고서는 GS건설이 취해야 할 차별화 포인트와 방어 포인트를 함께 적는다.
- 출처는 자료명 또는 URL 수준으로 특정하고 기준 시점을 함께 적는다.
- 데이터가 비어 있으면 단정하지 말고, 필요한 추가 확인 항목을 적는다.

## STEP12 Review Standard

STEP12에서는 아래 5개 기준으로 A/B/C 평가한다. 보고서 유형에 따라 세부 기준이 다르다.

### 아파트 시장조사

| 기준 | 고평가 조건 |
|---|---|
| 데이터 신뢰성 | 가격·거래 데이터에 출처(국토부·KB·R-ONE 등)와 기준 시점이 명시됐다 |
| 시장 해석 | 가격 흐름과 수요·공급 변화가 인과관계로 설명됐다 |
| 입지 분석 | 교통·학군·생활권이 타깃 수요층과 구체적으로 연결됐다 |
| 리스크 반영 | 대출 규제·입주 물량·금리 등 하방 리스크가 구조화됐다 |
| 결론 실효성 | 분양가 판단·수주 타당성·실행 방향이 근거와 함께 명확히 제시됐다 |

### 상가 시장조사

| 기준 | 고평가 조건 |
|---|---|
| 데이터 신뢰성 | 임대료·공실·매매가 데이터에 출처와 기준 시점이 명시됐다 |
| 시장 해석 | 상권 흐름·수요층·업종 구성이 분양성과 연결되어 설명됐다 |
| 입지 분석 | 가시성·동선·층별 집객력이 배후 수요층과 구체적으로 연결됐다 |
| 리스크 반영 | 공실 장기화·업종 편중·동선 분리 등 상가 고유 리스크가 구조화됐다 |
| 결론 실효성 | 층별 적정 평단가 밴드(1층 핵심/비핵심, 비1층 목적형/일반형)가 수치로 제시됐다 |

## Script Notes

`03_code/` 스크립트 사용 시 아래를 기억한다.

- `multi_model_evaluate.py`: **STEP12** 리뷰 패킷 생성 + Iteration 누적. `--reviewer` 미지정 시 폴더명에서 에이전트 태그 자동 감지. 폴더명에 태그가 없으면 `--reviewer [에이전트명]` 명시.
- `md_to_docx_converter.py`: **STEP13** MD→DOCX 변환. `_KR` 접미사 기준 한국어 설정 자동 적용.
- `improve_docx_design.py`: **STEP13** 디자인 보정. 작업 폴더에 `report_designed_[agent].docx` 생성 + `05_output/`에도 배치.
- `count_docx_chars.py`: **STEP13·STEP14** DOCX 문자수 검증. 목표 8,000~12,000자.
- `count_chars.py`: **STEP11** Markdown 초안 문자수 예비 검증.
- `insert_images.py`: 이미지 플레이스홀더 감지 후 삽입.
- `analyze_docx.py`: DOCX 구조 분석.

## Execution Notes

- Python 스크립트는 반드시 프로젝트 루트의 `.venv`를 사용해 실행한다.
- `.venv`가 없으면 먼저 `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`로 생성한다.
- 모든 스크립트 실행은 `source .venv/bin/activate` 없이 `.venv/bin/python` 으로 직접 호출한다.

  ```bash
  # DOCX 변환 표준 실행 순서 (매번 이 순서로 실행)
  .venv/bin/python 03_code/md_to_docx_converter.py [target_id] --input [STEP11 파일명]
  .venv/bin/python 03_code/improve_docx_design.py [input.docx] [output.docx]
  .venv/bin/python 03_code/count_docx_chars.py [output.docx]
  ```

- 명령 예시와 프로젝트 전반 설명은 [`README.md`](README.md)를 참조한다.
- 프로젝트 배경 설명이 더 필요하면 [`00_ref/부동산_분석_프로젝트_개요.md`](00_ref/부동산_분석_프로젝트_개요.md), [`00_ref/부동산_분석_프로젝트_전략.md`](00_ref/부동산_분석_프로젝트_전략.md)를 읽는다.
