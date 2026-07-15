"""STEP11 Markdown 초안 문자수 예비 검증

주 지표는 표 포함·공백 포함 문자수(DOCX 게이트와 동일 축)다.
정식 판정은 STEP13 이후 count_docx_chars.py 결과를 기준으로 한다.

사용 예:
    python 03_code/count_chars.py 04_workspace/[폴더명]/STEP11_아파트보고서_draft.md
    python 03_code/count_chars.py [파일경로] --min 8000 --max 12000
"""
import argparse
import sys
from pathlib import Path

from _common import (
    EXIT_ERROR,
    EXIT_OK,
    EXIT_PARTIAL,
    configure_stdout,
    count_text_chars,
    strip_markdown,
)


def main():
    configure_stdout()
    parser = argparse.ArgumentParser(description="Markdown 문자수 예비 검증")
    parser.add_argument("path", help="Markdown 파일 경로")
    parser.add_argument("--min", type=int, help="하한 임계값 (지정 시 범위 판정)")
    parser.add_argument("--max", type=int, help="상한 임계값 (지정 시 범위 판정)")
    args = parser.parse_args()

    path = Path(args.path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"ERROR: 파일을 읽을 수 없습니다: {path} ({e})", file=sys.stderr)
        sys.exit(EXIT_ERROR)

    with_tables = count_text_chars(strip_markdown(text, include_tables=True))
    no_tables = count_text_chars(strip_markdown(text, include_tables=False))

    print(f"=== MD 예비 문자수: {path.name} ===")
    print(f"전체(공백포함): {with_tables.total:,}  <- 게이트 판정과 동일 축 (개산)")
    print(f"전체(공백제외): {with_tables.no_space:,}")
    print(f"표 제외(공백포함): {no_tables.total:,}")
    print(f"표 제외(공백제외): {no_tables.no_space:,}")
    print("정식 판정은 count_docx_chars.py (STEP13/14) 결과를 기준으로 한다.")

    if args.min is not None or args.max is not None:
        lo = args.min if args.min is not None else 0
        hi = args.max if args.max is not None else float("inf")
        if lo <= with_tables.total <= hi:
            print(f"예비 판정: [OK] 범위 내 ({lo:,}~{hi:,})")
        else:
            print(f"예비 판정: [OUT] 범위 밖 ({lo:,}~{hi:,})")
            sys.exit(EXIT_PARTIAL)

    sys.exit(EXIT_OK)


if __name__ == "__main__":
    main()
