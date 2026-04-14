# Housing Market Research

한국 주택시장 조사와 사업지 검토를 위한 리서치 워크스페이스다. 권역 브리프, 사업지 입지 분석, 경쟁 단지 비교를 빠르게 만들 수 있도록 구성했다.

## 목적

- 권역별 주택시장 브리프 작성
- 신규 사업지 입지 검토
- 경쟁 단지 비교표와 해설 작성
- 정책 변화가 분양성에 미치는 영향 정리
- Markdown 초안을 DOCX 보고서로 변환

## 시작 순서

1. [04_plan/주택시장조사_마스터_워크플로우.md](04_plan/주택시장조사_마스터_워크플로우.md)를 읽는다.
2. 아래 템플릿 중 하나를 고른다.
   - [04_plan/템플릿_권역시장브리프.md](04_plan/템플릿_권역시장브리프.md)
   - [04_plan/템플릿_사업지입지분석.md](04_plan/템플릿_사업지입지분석.md)
   - [04_plan/템플릿_경쟁단지비교.md](04_plan/템플릿_경쟁단지비교.md)
3. `06_middle_output/[target_id]_KR/` 폴더를 만든다.
4. 중간 산출물을 작성하고 필요하면 DOCX로 변환한다.

## 디렉터리 구조

```text
housing-market-research/
├── 00_ref/                    # 개요·전략 문서
├── 01_data/                   # 원천 데이터 보관
├── 04_plan/                   # 워크플로우와 템플릿
├── 05_code/                   # DOCX 변환·이미지 삽입 등 유틸
├── 06_middle_output/          # 권역/사업지별 작업공간
└── 07_final_output_kr/        # 최종 보고서
```

## 핵심 문서

- 프로젝트 개요: [00_ref/부동산_분석_프로젝트_개요.md](00_ref/부동산_분석_프로젝트_개요.md)
- 프로젝트 전략: [00_ref/부동산_분석_프로젝트_전략.md](00_ref/부동산_분석_프로젝트_전략.md)
- 주택시장조사 마스터: [04_plan/주택시장조사_마스터_워크플로우.md](04_plan/주택시장조사_마스터_워크플로우.md)
- 권역 브리프 템플릿: [04_plan/템플릿_권역시장브리프.md](04_plan/템플릿_권역시장브리프.md)
- 사업지 입지 템플릿: [04_plan/템플릿_사업지입지분석.md](04_plan/템플릿_사업지입지분석.md)
- 경쟁 단지 비교 템플릿: [04_plan/템플릿_경쟁단지비교.md](04_plan/템플릿_경쟁단지비교.md)
- 샘플 리포트: [06_middle_output/seongsu-residential_KR/STEP11_보고서_draft.md](06_middle_output/seongsu-residential_KR/STEP11_보고서_draft.md)

## 빠른 예시

```bash
mkdir -p 06_middle_output/songpa-jamsil_KR/images

python 05_code/md_to_docx_converter.py songpa-jamsil_KR \
  --title "송파·잠실 권역 주택시장 브리프"
```

## 코드 재사용 범위

다음 스크립트는 도메인과 무관하게 그대로 쓸 수 있다.

- `05_code/md_to_docx_converter.py`
- `05_code/insert_images.py`
- `05_code/improve_docx_design.py`
- `05_code/count_docx_chars.py`

