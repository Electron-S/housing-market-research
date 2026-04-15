"""mermaid로 생성한 이미지를 DOCX 부동산 분석 보고서에 삽입한다.

Usage:
    python insert_images.py 05_output/seongsu-residential_KR.docx
    python insert_images.py 05_output/seongsu-residential_KR.docx 05_output/seongsu-residential_KR_out.docx

분석대상 ID는 DOCX 파일명(stem)에서 자동 검출한다.
이미지는 04_workspace/<분석대상 ID>/images/ 하위의 causal.png, kpi_tree.png를 사용.

삽입 로직:
  - 「※그림1은 별도 이미지로 삽입」 등의 플레이스홀더 단락을 이미지로 치환
  - 플레이스홀더가 없으면 「그림1」「그림2」 캡션 단락의 직후에 삽입
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Mm, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

ROOTDIR = Path(__file__).resolve().parent.parent

# 플레이스홀더 패턴 (부분 일치)
PLACEHOLDER_PATTERNS = [
    # (검색 패턴, 이미지 키)
    (re.compile(r"※.*図1.*画像.*挿入"), "causal"),
    (re.compile(r"※.*図2.*画像.*挿入"), "kpi"),
    (re.compile(r"※.*그림\s*1.*이미지.*삽입"), "causal"),
    (re.compile(r"※.*그림\s*2.*이미지.*삽입"), "kpi"),
]

# 플레이스홀더가 없는 경우의 폴백: 캡션 행 직후에 삽입
CAPTION_PATTERNS = [
    (re.compile(r"^図1[：:]"), "causal"),
    (re.compile(r"^図2[：:]"), "kpi"),
    (re.compile(r"^그림\s*1[：:]"), "causal"),
    (re.compile(r"^그림\s*2[：:]"), "kpi"),
]


def extract_target_id(docx_path: str) -> str:
    """DOCX 파일명에서 분석대상 ID를 추출한다 (_designed 접미사 제거)"""
    name = Path(docx_path).stem  # 예: "seongsu-residential_KR" 또는 "seongsu-residential_KR_designed"
    return re.sub(r'_designed$', '', name)


def resolve_image_paths(target_id: str) -> dict:
    """분석대상 ID로부터 이미지 경로를 해석한다"""
    img_dir = ROOTDIR / "04_workspace" / target_id / "images"
    if not img_dir.exists():
        # _KR 접미사 없는 경우도 탐색
        bare = re.sub(r'_KR$', '', target_id)
        alt_dir = ROOTDIR / "04_workspace" / bare / "images"
        if alt_dir.exists():
            img_dir = alt_dir
    paths = {
        "causal": img_dir / "causal.png",
        "kpi": img_dir / "kpi_tree.png",
    }
    for path in paths.values():
        if not path.exists():
            print(f"WARNING: 이미지 파일을 찾을 수 없음: {path}")
    return paths


def insert_image_at_paragraph(p, img_path, width_mm=145):
    """단락의 텍스트를 지우고 이미지로 치환한다"""
    p.clear()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = p.add_run()
    run.add_picture(str(img_path), width=Mm(width_mm))


def add_image_after_paragraph(doc, p, img_path, caption_text, width_mm=145):
    """단락 직후에 이미지와 캡션을 추가한다"""
    # 이미지 단락
    img_p = doc.add_paragraph()
    p._element.addnext(img_p._element)
    img_p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = img_p.add_run()
    run.add_picture(str(img_path), width=Mm(width_mm))

    # 캡션 단락
    cap_p = doc.add_paragraph()
    img_p._element.addnext(cap_p._element)
    cap_p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    cap_run = cap_p.add_run(caption_text)
    cap_run.font.size = Pt(9)


def insert_images(docx_path, output_path, image_paths):
    doc = Document(docx_path)

    inserted = {"causal": False, "kpi": False}

    # Phase 1: 플레이스홀더 단락을 이미지로 치환
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue
        for pattern, key in PLACEHOLDER_PATTERNS:
            if not inserted[key] and pattern.search(text) and image_paths[key].exists():
                insert_image_at_paragraph(p, image_paths[key])
                inserted[key] = True
                print(f"Inserted {key} image (placeholder replacement): {image_paths[key].name}")

    # Phase 2: 플레이스홀더를 찾지 못한 경우 캡션 행 직후에 삽입
    if not all(inserted.values()):
        for p in doc.paragraphs:
            text = p.text.strip()
            if not text:
                continue
            for pattern, key in CAPTION_PATTERNS:
                if not inserted[key] and pattern.search(text) and image_paths[key].exists():
                    add_image_after_paragraph(doc, p, image_paths[key], text)
                    inserted[key] = True
                    print(f"Inserted {key} image (after caption): {image_paths[key].name}")

    # 결과 요약
    for key, done in inserted.items():
        if not done:
            img = image_paths.get(key)
            if img and img.exists():
                print(f"WARNING: {key} image was NOT inserted (no matching text found in document)")
            else:
                print(f"SKIP: {key} image file does not exist")

    doc.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python insert_images.py <docx_path> [output_path]")
        print("Example: python insert_images.py 05_output/184226.docx")
        sys.exit(1)

    docx_in = sys.argv[1]
    docx_out = sys.argv[2] if len(sys.argv) > 2 else docx_in

    target_id = extract_target_id(docx_in)
    print(f"분석 대상: {target_id}")

    image_paths = resolve_image_paths(target_id)
    insert_images(docx_in, docx_out, image_paths)
