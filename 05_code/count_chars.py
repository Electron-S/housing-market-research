import re
import sys

filepath = sys.argv[1] if len(sys.argv) > 1 else "06_middle_output/035890_KR/STEP11_제안서_draft.md"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

# Non-table lines (wc-m style, includes whitespace)
non_table_lines = [l for l in lines if not l.strip().startswith("|") and l.strip() != "---"]
non_table_text = "\n".join(non_table_lines)
non_table_wc = len(non_table_text)
print(f"Non-table wc-m: {non_table_wc}")

# Non-table chars (no whitespace, no markdown)
clean = re.sub(r"[#*]", "", non_table_text)
clean_nows = re.sub(r"\s", "", clean)
print(f"Non-table chars (no ws/md): {len(clean_nows)}")

# Total wc-m
print(f"Total wc-m: {len(text)}")

# All chars no whitespace
all_clean = re.sub(r"[#*]", "", text)
all_nows = re.sub(r"\s", "", all_clean)
print(f"All chars (no ws/md): {len(all_nows)}")
