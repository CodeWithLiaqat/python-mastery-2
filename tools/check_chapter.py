"""QA script: chapter ke tamam .py files chalata hai aur Urdu script ke liye scan karta hai.

Usage: python tools/check_chapter.py chapters/ch01-python-ka-taaruf
Jo files jaan boojh kar error dikhati hain unke naam mein 'error', 'zero_division'
ya 'traceback' hota hai; unka non-zero exit expected hai.
"""
import re
import subprocess
import sys
from pathlib import Path

EXPECTED_ERROR_MARKERS = ("error", "zero_division", "traceback")
URDU_SCRIPT = re.compile(r"[؀-ۿ]")


def main() -> int:
    chapter = Path(sys.argv[1])
    failures = 0
    for py in sorted(chapter.rglob("*.py")):
        result = subprocess.run([sys.executable, py.name], cwd=py.parent,
                                capture_output=True, text=True, timeout=60)
        expect_error = any(m in py.stem for m in EXPECTED_ERROR_MARKERS)
        ok = (result.returncode != 0) if expect_error else (result.returncode == 0)
        print(f"{'PASS' if ok else 'FAIL'}  {py.relative_to(chapter)}")
        failures += not ok
    for f in sorted(chapter.rglob("*")):
        if f.suffix in {".md", ".py"} and URDU_SCRIPT.search(f.read_text(encoding="utf-8")):
            print(f"FAIL  Urdu script mila: {f}")
            failures += 1
    print(f"\n{'Sab theek!' if failures == 0 else f'{failures} masle mile.'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
