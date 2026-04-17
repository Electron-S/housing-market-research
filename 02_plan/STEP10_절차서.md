# STEP 10: 보고서 집필

## 목적
STEP1~9의 내용을 독자가 읽기 쉬운 보고서 구조로 재편한다.
사실·해석·판단을 명확히 구분하고, 결론을 서두에 배치한다.

## 입력
- STEP1~9 output 전체
- 산출물 유형에 맞는 템플릿:
  - `02_plan/템플릿_권역시장브리프.md`
  - `02_plan/템플릿_사업지입지분석.md`
  - `02_plan/템플릿_경쟁단지비교.md`

## 작업 체크리스트
- [ ] 산출물 유형 확인 후 해당 템플릿 선택
- [ ] STEP9 결론을 Executive Summary에 배치 (두괄식)
- [ ] STEP2~8 내용을 보고서 섹션으로 재편
- [ ] 사실·해석·판단을 문장 단위로 분리
- [ ] 모든 수치에 출처와 기준 시점 재확인
- [ ] 광고성 문구 제거 점검
- [ ] 분량 확인: 한국어 10,000~15,000자 권장
- [ ] STEP0 인계 내용(사업 단계·GS 포지션)을 서론 또는 사업 개요에 반영
- [ ] STEP0의 수주 전/후에 따라 보고서 결론 방향 확인
  - **수주 후:** GS건설 분양·임대 실행안 포함
  - **수주 전:** GS건설 수주 제안 조건 및 타당성 판단 포함
- [ ] 분양가 제안이 `약간 공격적` 기조인지 재확인
- [ ] 상가 시장조사인 경우 STEP9의 `층별 적정 평단가 밴드 표`가 본문에 실제 삽입됐는지 확인
- [ ] 상가 시장조사인 경우 숫자형 가격 밴드 없이 `공격적/보수적` 같은 정성 표현만 남아 있지 않은지 확인
- [ ] 파일명 규칙 준수

## 파일명 규칙
| 산출물 유형 | 파일명 |
|---|---|
| 아파트 시장조사 보고서 | `STEP11_아파트보고서_draft.md` |
| 상가 시장조사 보고서 | `STEP11_상가보고서_draft.md` |
| 권역 시장 브리프 | `STEP11_권역브리프_draft.md` |
| 사업지 입지 분석 | `STEP11_사업지분석_draft.md` |
| 경쟁 단지 비교 | `STEP11_경쟁비교_draft.md` |

## 산출물
`04_workspace/[target_id]_[agent]_KR/STEP11_[유형]_draft.md`

### 기본 보고서 구조 (`STEP11_[유형]_draft.md`)
```markdown
# [대상] 부동산 분석 보고서

## Executive Summary (결론 우선)
## 1. 거시·정책 환경
## 2. 가격·거래 추이
## 3. 수요 분석
## 4. 공급 분석
## 5. 입지 분석
## 6. 경쟁 비교
## 7. 리스크
## 8. 결론 및 시사점
```

## 이후 변환 절차
```bash
# DOCX 변환
python 03_code/md_to_docx_converter.py [target_id]_[agent]_KR --title "[대상] 부동산 분석 보고서"

# 디자인 보정
python 03_code/improve_docx_design.py 04_workspace/[target_id]_[agent]_KR/report_draft_[agent].docx

# STEP12 리뷰 패킷 생성
python 03_code/multi_model_evaluate.py [target_id]_[agent]_KR --reviewer codex
```

> 최종 DOCX는 디자인 보정 이후 `05_output/`에 저장한다.
> 스크립트는 가상환경에서 실행하고, `STEP11_보고서_draft.md`가 없더라도 `STEP11_*_draft.md`를 자동 탐색한다.
