# STEP12: 품질 리뷰 (MD 단계)

## 목적

STEP11에서 작성한 보고서 초안(Markdown)을 **실행 중인 에이전트가 직접** 5개 기준으로 평가하고,
기준 미달 항목을 수정해 PASS 등급까지 반복한다.
에이전트별 리뷰 결과를 누적 기록해, 추후 Codex·Claude·기타 에이전트 간 보고서 품질 비교에 사용한다.

## 에이전트별 실행 원칙

- **Codex에서 실행 시**: Codex가 보고서를 작성했고, Codex가 품질 검증을 수행한다. `--reviewer codex`
- **Claude에서 실행 시**: Claude가 보고서를 작성했고, Claude가 품질 검증을 수행한다. `--reviewer claude`
- 리뷰 결과 파일은 에이전트별로 분리된다: `STEP12_output_codex.md`, `STEP12_output_claude.md`
- 외부 API 호출 없음. 실행 중인 에이전트가 보고서 원문을 직접 읽고 판단한다.

## 입력

- `STEP11_[유형]_draft.md`
- `STEP1~STEP10_output.md` (검증 시 참조)

## 실행 절차

### Step 1. 리뷰 패킷 생성

```bash
.venv/bin/python 03_code/multi_model_evaluate.py [target_id]_[agent]_KR --reviewer [에이전트명]
# 예시
.venv/bin/python 03_code/multi_model_evaluate.py hanam-regenheim_codex_KR --reviewer codex
.venv/bin/python 03_code/multi_model_evaluate.py hanam-regenheim_claude_KR --reviewer claude
```

생성 파일:
- `STEP12_review_packet_[agent].md` — 보고서 원문 + 평가 기준 + 기록 템플릿
- `STEP12_output_[agent].md` — 결과 누적 파일 (없으면 자동 생성)

### Step 2. 보고서 평가

리뷰 패킷을 읽고 아래 5개 기준을 각각 A/B/C로 평가한다.

| 번호 | 평가항목 | 고평가 기준 |
|---|---|---|
| 1 | 데이터 신뢰성 | 가격·거래 수치에 출처(국토부·KB·R-ONE 등)와 기준 시점이 명시됐는가 |
| 2 | 시장 해석 | 가격 흐름과 수요·공급 변화가 인과관계로 설명됐는가 |
| 3 | 입지 분석 | 교통·학군·생활권이 실수요층과 구체적으로 연결됐는가 |
| 4 | 리스크 반영 | 대출 규제·입주 물량·금리 변화 등 하방 리스크가 구조화됐는가 |
| 5 | 결론 실효성 | 분양가 판단·수주 타당성·실행 방향이 근거와 함께 명확히 제시됐는가 |

### Step 3. 결과 기록

`STEP12_output_[agent].md`에 아래 형식으로 Iteration을 추가한다.

```markdown
### Iteration N (YYYY-MM-DD)

#### 메타정보
- Reviewer: [에이전트명]
- Source: `[파일 경로]`

#### 종합평가
- Overall: A/B/C
- Reason: 한두 문장 요약

#### 평가결과 요약
| 평가항목 | 등급 | 코멘트 |
|---|---|---|
| 데이터 신뢰성 | | |
| 시장 해석 | | |
| 입지 분석 | | |
| 리스크 반영 | | |
| 결론 실효성 | | |

#### 강점
-
-

#### 개선 필요 항목
-
-

#### 수정 지시
-
-

#### 반복 판정
- Status: PASS / REVISE
- Next Action:
```

### Step 4. 반복 또는 종료 판단

| 판정 | 조건 | 다음 행동 |
|---|---|---|
| **PASS** | 5개 항목 전부 A | STEP13 진행 |
| **REVISE** | A 미달 항목 있음 | STEP11 초안 수정 → 스크립트 재실행 (Iteration +1) |

- 최대 3 Iteration. 3회 후에도 REVISE면 미달 항목을 명시하고 STEP13으로 진행하되 보고서 한계를 기록한다.
- Iteration 번호는 스크립트가 `STEP12_output_[agent].md`를 읽어 자동 증가한다.

## 산출물

- `04_workspace/[target_id]_[agent]_KR/STEP12_review_packet_[agent].md`
- `04_workspace/[target_id]_[agent]_KR/STEP12_output_[agent].md`

## 다음 단계

STEP12 PASS → **STEP13 MD→DOCX 변환** 진행
