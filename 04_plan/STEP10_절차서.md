# STEP 10: 보고서 집필

## 목적
STEP1~9의 내용을 독자가 읽기 쉬운 보고서 구조로 재편한다.
사실·해석·판단을 명확히 구분하고, 결론을 서두에 배치한다.

## 입력
- STEP1~9 output 전체
- 산출물 유형에 맞는 템플릿:
  - `04_plan/템플릿_권역시장브리프.md`
  - `04_plan/템플릿_사업지입지분석.md`
  - `04_plan/템플릿_경쟁단지비교.md`

## 작업 체크리스트
- [ ] 산출물 유형 확인 후 해당 템플릿 선택
- [ ] STEP9 결론을 Executive Summary에 배치 (두괄식)
- [ ] STEP2~8 내용을 보고서 섹션으로 재편
- [ ] 사실·해석·판단을 문장 단위로 분리
- [ ] 모든 수치에 출처와 기준 시점 재확인
- [ ] 광고성 문구 제거 점검
- [ ] 분량 확인: 한국어 6,000~12,000자 권장
- [ ] 파일명 규칙 준수

## 파일명 규칙
| 산출물 유형 | 파일명 |
|---|---|
| 권역 시장 브리프 | `STEP10_권역브리프_draft.md` |
| 사업지 입지 분석 | `STEP10_사업지분석_draft.md` |
| 경쟁 단지 비교 | `STEP10_경쟁비교_draft.md` |

## 산출물
`06_middle_output/[target_id]_KR/STEP10_[유형]_draft.md`

### 기본 보고서 구조
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
python 05_code/md_to_docx_converter.py [target_id]_KR --title "[대상] 부동산 분석 보고서"

# 디자인 보정
python 05_code/improve_docx_design.py 07_final_output_kr/[target_id].docx

# AI 품질 평가
python 05_code/multi_model_evaluate.py [target_id]_KR
```
