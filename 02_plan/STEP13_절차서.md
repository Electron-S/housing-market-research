# STEP13: MD→DOCX 변환

## 목적

STEP12 PASS를 받은 Markdown 초안을 Word 문서로 변환하고, 디자인 보정 후 문자수를 검증한다.

## 입력

- `STEP11_[유형]_draft.md` (STEP12 PASS 확인 후)

## 실행 절차

모든 스크립트는 프로젝트 루트의 `.venv`를 사용한다.

### Step 1. MD → DOCX 변환

```bash
.venv/bin/python 03_code/md_to_docx_converter.py [target_id]_[agent]_KR \
  --input STEP11_[유형]_draft.md
```

- `_KR` 접미사 기준으로 한국어 설정 자동 적용
- 출력: `04_workspace/[target_id]_[agent]_KR/report_draft_[agent].docx`

### Step 2. 디자인 보정

```bash
.venv/bin/python 03_code/improve_docx_design.py \
  04_workspace/[target_id]_[agent]_KR/report_draft_[agent].docx \
  04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx
```

- 제목 스타일, 표 헤더 배경색, 테두리선, 헤더/푸터, 페이지 번호 적용
- 출력: `report_designed_[agent].docx` (작업 폴더) + `05_output/[target_id]_designed.docx` (최종 출력 폴더)

### Step 3. 문자수 검증

```bash
.venv/bin/python 03_code/count_docx_chars.py \
  04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx
```

| 결과 | 조치 |
|---|---|
| 8,000~12,000자 | STEP14 진행 |
| 8,000자 미만 | STEP11로 복귀 — 분석 내용 보강 후 STEP12 재수행 |
| 12,000자 초과 | STEP11로 복귀 — 중복 내용 제거 후 STEP12 재수행 |

> 문자수 미달·초과 시 STEP12를 건너뛰지 않는다. 내용 변경이 발생했으므로 품질 리뷰를 반드시 재수행한다.

## 체크리스트

- [ ] `report_draft_[agent].docx` 생성 확인
- [ ] `report_designed_[agent].docx` 생성 확인
- [ ] `05_output/[target_id]_designed.docx` 생성 확인
- [ ] 문자수 8,000~12,000자 범위 확인

## 산출물

- `04_workspace/[target_id]_[agent]_KR/report_draft_[agent].docx`
- `04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx`
- `05_output/[target_id]_designed.docx`

## 다음 단계

문자수 통과 → **STEP14 품질 리뷰 (DOCX 단계)** 진행
