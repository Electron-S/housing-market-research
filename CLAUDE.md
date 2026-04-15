# CLAUDE.md

This file is the operating guide for Claude Code in this repository.

## What Claude Should Do

- 사람용 개요나 실행 예시가 필요하면 [`README.md`](README.md)를 본다.
- 실제 작업 절차의 정본은 [`02_plan/주택시장조사_마스터_워크플로우.md`](02_plan/주택시장조사_마스터_워크플로우.md)다.
- Claude는 이 문서를 "행동 규칙"으로 사용하고, 프로젝트 설명은 반복하지 않는다.

## Required Reading Order

보고서 작성 또는 STEP 진행 요청을 받으면 아래 순서를 지킨다.

1. [`02_plan/주택시장조사_마스터_워크플로우.md`](02_plan/주택시장조사_마스터_워크플로우.md)를 먼저 읽어 산출물 유형과 전체 플로우를 파악한다.
2. 현재 요청이 어떤 산출물인지 특정한다.
3. 필요한 STEP에 들어가기 직전에 해당 `02_plan/STEPx_절차서.md`만 읽는다.
4. 아직 `04_workspace/공통_KR/`가 없고 STEP0 선행이 필요한 작업이면 STEP0부터 시작한다.

금지:

- STEP1~STEP10 절차서를 한 번에 미리 읽기
- 출처와 기준 시점 없이 수치 단정하기
- 근거 없이 분양가나 분양성 결론 내리기

## Output Rules

- 작업 폴더는 `04_workspace/[target_id]_[agent]_KR/`를 기본으로 사용한다.
- 중간 산출물은 `STEP1_output.md`부터 `STEP10_output.md`까지 저장한다.
- 집필 파일은 `STEP11_[유형]_draft.md` 형식을 사용한다.
- 리뷰 패킷은 `STEP12_review_packet_[agent].md`, 리뷰 결과는 `STEP12_output_[agent].md`를 사용한다.
- DOCX 초안은 `report_draft_[agent].docx`, 최종본은 `report_designed_[agent].docx`를 사용한다.

## Analysis Rules

1. 모든 수치에는 기준 시점과 출처를 적는다.
2. 사실, 해석, 판단을 분리해서 쓴다.
3. 확실하지 않은 내용은 추정이라고 명시한다.
4. 비교 단지 선정 근거를 반드시 적는다.
5. 입지 설명은 교통, 학군, 인프라를 수요층과 연결해서 쓴다.
6. 정책 변수와 공급 리스크를 빠뜨리지 않는다.
7. 결론은 실행 가능한 문장으로 쓴다.

## Writing Rules

- 광고 문구처럼 쓰지 않는다.
- 추상적 시장 설명보다 가격, 수요, 공급, 흡수 가능성 판단을 우선한다.
- 출처는 자료명 또는 URL 수준으로 특정하고 기준 시점을 함께 적는다.
- 데이터가 비어 있으면 단정하지 말고, 필요한 추가 확인 항목을 적는다.

## STEP12 Review Standard

STEP12에서는 아래 5개 기준으로 A/B/C 평가한다.

| 기준 | 고평가 조건 |
|---|---|
| 데이터 신뢰성 | 가격·거래 데이터에 출처와 기준 시점이 명시되어 있다 |
| 입지 분석 | 입지 요소가 타깃 수요층과 구체적으로 연결되어 있다 |
| 비교 단지 적정성 | 선정 근거와 가격 차등 근거가 명확하다 |
| 분양가 산정 근거 | 지수 적용 방법과 결과값 연결이 논리적이다 |
| 결론 실효성 | 분양가 및 분양성 판단이 실행 가능한 수준이다 |

## Script Notes

`03_code/` 스크립트 사용 시 아래를 기억한다.

- `md_to_docx_converter.py`: `_KR` 접미사 기준으로 한국어 설정을 자동 적용한다.
- `insert_images.py`: 한국어 이미지 플레이스홀더를 감지해 삽입한다.
- `improve_docx_design.py`: 디자인 보정 후 기본적으로 `report_designed_[agent].docx`를 생성한다.
- `count_docx_chars.py`: DOCX 문자수를 검증한다.
- `count_chars.py`: Markdown 초안 문자수를 검증한다.
- `analyze_docx.py`: DOCX 구조를 분석한다.
- `multi_model_evaluate.py`: STEP12 리뷰 패킷과 반복 리뷰 준비를 돕는다.

## Execution Notes

- Python 스크립트는 가상환경 활성화 후 실행한다.
- 명령 예시와 프로젝트 전반 설명은 [`README.md`](README.md)를 참조한다.
- 프로젝트 배경 설명이 더 필요하면 [`00_ref/부동산_분석_프로젝트_개요.md`](00_ref/부동산_분석_프로젝트_개요.md), [`00_ref/부동산_분석_프로젝트_전략.md`](00_ref/부동산_분석_프로젝트_전략.md)를 읽는다.
