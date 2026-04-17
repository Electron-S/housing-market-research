# STEP15: 최종화

## 목적

STEP14 PASS 후 최종 DOCX를 `05_output/`에 확정 배치하고, 파일명·백업·산출물 목록을 정리한다.

## 입력

- `04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx` (STEP14 PASS 확인 후)

## 실행 절차

### Step 1. 최종 파일 배치 확인

`improve_docx_design.py`가 이미 `05_output/`에 복사본을 만들어 두므로, 파일 존재 여부를 확인한다.

```bash
ls 05_output/
```

- 파일명 기본: `[target_id]_designed.docx`
- 예시: `hanam-regenheim_claude_KR_designed.docx`

파일이 없으면 수동 복사:
```bash
cp 04_workspace/[target_id]_[agent]_KR/report_designed_[agent].docx \
   05_output/[target_id]_designed.docx
```

### Step 2. 최종 체크리스트

- [ ] `05_output/[target_id]_designed.docx` 존재 확인
- [ ] 파일 열어서 표지·본문·결론 육안 확인
- [ ] STEP12 REVISE 지적 사항이 최종본에 반영됐는가
- [ ] STEP14 미통과 항목이 없는가
- [ ] 문자수 8,000~12,000자 최종 확인

### Step 3. 사용자 요청 시 외부 드라이브 복사

```bash
# 예: D 드라이브 복사 (WSL 환경)
cp 05_output/[target_id]_designed.docx /mnt/d/[파일명].docx
```

## 산출물 최종 목록

| 파일 | 위치 | 설명 |
|---|---|---|
| `STEP0~STEP10_output.md` | `04_workspace/[target_id]_[agent]_KR/` | 분석 중간 산출물 |
| `STEP11_[유형]_draft.md` | `04_workspace/[target_id]_[agent]_KR/` | 보고서 Markdown 초안 |
| `STEP12_review_packet_[agent].md` | `04_workspace/[target_id]_[agent]_KR/` | MD 품질 리뷰 패킷 |
| `STEP12_output_[agent].md` | `04_workspace/[target_id]_[agent]_KR/` | MD 품질 리뷰 결과 누적 |
| `STEP14_output.md` | `04_workspace/[target_id]_[agent]_KR/` | DOCX 검증 결과 |
| `report_draft_[agent].docx` | `04_workspace/[target_id]_[agent]_KR/` | 변환 초안 DOCX |
| `report_designed_[agent].docx` | `04_workspace/[target_id]_[agent]_KR/` | 디자인 보정 DOCX |
| **`[target_id]_designed.docx`** | **`05_output/`** | **최종 납품 파일** |

## STEP15_output.md 기록 형식

```markdown
## STEP15 최종화 완료

- 완료 일시: YYYY-MM-DD
- 최종 파일: `05_output/[target_id]_designed.docx`
- 문자수: [N]자
- STEP12 Iteration 수: [N]회
- 에이전트: [claude / codex]
- 특이사항: (있을 경우 기록)
```
