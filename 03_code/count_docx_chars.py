"""DOCX 문자수 카운터 (크로스플랫폼, python-docx 기반)

- 본문 + 표 + 머리글/바닥글 모두 카운트 (게이트 정본 정의)
- 언어별 규정 임계값 체크 (ko: 8,000~12,000, 공백 포함 기준)
- 종료코드: 0=범위 내, 1=파일오류, 2=범위 밖

사용 예:
    python 03_code/count_docx_chars.py 04_workspace/[폴더명]/report_designed_[agent].docx
    python 03_code/count_docx_chars.py path.docx --lang ko
    python 03_code/count_docx_chars.py path.docx --min 9000 --max 13000
"""
import argparse
import sys
from pathlib import Path

from _common import (
    CHAR_LIMITS,
    EXIT_ERROR,
    EXIT_OK,
    EXIT_PARTIAL,
    configure_stdout,
    count_docx_chars,
)


def main():
    configure_stdout()
    parser = argparse.ArgumentParser(description='DOCX 문자수 카운터 (ko)')
    parser.add_argument('path', help='DOCX 파일 경로')
    parser.add_argument('--lang', choices=['ko'], default='ko', help='언어 (기본: ko)')
    parser.add_argument('--min', type=int, help='하한 임계값 (기본 언어별)')
    parser.add_argument('--max', type=int, help='상한 임계값 (기본 언어별)')
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f'ERROR: 파일 없음: {path}', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    lo, hi = CHAR_LIMITS[args.lang]
    if args.min is not None:
        lo = args.min
    if args.max is not None:
        hi = args.max

    try:
        count = count_docx_chars(path)
    except Exception as e:
        print(f'ERROR: DOCX 읽기 실패: {path} ({e})', file=sys.stderr)
        sys.exit(EXIT_ERROR)

    print(f'=== Character Count: {path.name} ===')
    print(f'언어 기준: {args.lang}')
    print(f'문자수(공백포함): {count.total:,}')
    print(f'문자수(공백제외): {count.no_space:,}')
    print(f'규정 범위: {lo:,}~{hi:,} (공백포함 기준)')

    if lo <= count.total <= hi:
        print('결과: [OK] 범위 내')
        sys.exit(EXIT_OK)
    elif count.total < lo:
        print(f'결과: [UNDER] {lo - count.total:,}자 부족')
        sys.exit(EXIT_PARTIAL)
    else:
        print(f'결과: [OVER] {count.total - hi:,}자 초과')
        sys.exit(EXIT_PARTIAL)


if __name__ == '__main__':
    main()
