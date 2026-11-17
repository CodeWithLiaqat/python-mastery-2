"""Chapter builder: README.src.md -> README.md

- ```python blocks jinki pehli line `# file: <path>` ho, woh file likhi aur chalayi jati hai.
- `<!-- stdin: a | b -->` block se theek pehle ho to woh values input() ko di jati hain.
- `@@OUT <path>@@` placeholder us file ke asal output se replace hota hai.
- Jis file ke naam mein 'error' ho uska non-zero exit expected hai.
Usage: python tools/build.py chapters/ch02-... [--show]
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BLOCK = re.compile(
    r"(?:<!-- stdin: (?P<stdin>.*?) -->\n)?```python\n# file: (?P<path>\S+)\n(?P<code>.*?)\n```", re.S)
URDU = re.compile(r"[؀-ۿ]")


def run(chapter: Path, rel: str, stdin: str | None) -> tuple[str, int]:
    f = chapter / rel
    env = dict(os.environ, PYTHONPATH=str(ROOT / "runtime"), PYTHONUNBUFFERED="1",
               MPLBACKEND="Agg", BOOK_ECHO_INPUT="1", PYTHONWARNINGS="default", COLUMNS="100")
    data = "\n".join(s.strip() for s in stdin.split("|")) + "\n" if stdin else ""
    r = subprocess.run([sys.executable, f.name], cwd=f.parent, input=data, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env, timeout=300)
    out = r.stdout.replace(str(f.parent.resolve()) + "/", ".../")
    out = re.sub(r'File "/[^"]*/(site-packages|lib/python3[^"]*)/', r'File ".../\1/', out)
    return out.rstrip("\n"), r.returncode


def main() -> int:
    chapter = Path(sys.argv[1]).resolve()
    show = "--show" in sys.argv
    src = (chapter / "README.src.md").read_text(encoding="utf-8")
    outputs, fails = {}, 0
    for m in BLOCK.finditer(src):
        rel = m["path"]
        p = chapter / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"# file: {rel}\n{m['code']}\n", encoding="utf-8")
        out, code = run(chapter, rel, m["stdin"])
        bad = (code == 0) if "error" in Path(rel).stem else (code != 0)
        outputs[rel] = out
        if bad:
            fails += 1
            print(f"FAIL {rel} (exit {code})\n{out}\n")
        elif show:
            lines = out.splitlines()
            print(f"--- {rel}\n" + "\n".join(lines[:12]) + ("\n  ..." if len(lines) > 12 else ""))
    def sub(m):
        if m[1] not in outputs:
            nonlocal fails
            fails += 1
            print(f"FAIL placeholder without file: {m[1]}")
            return m[0]
        return outputs[m[1]]
    final = re.sub(r"@@OUT (\S+)@@", sub, src)
    if URDU.search(final):
        fails += 1
        print("FAIL Urdu script found")
    (chapter / "README.md").write_text(final, encoding="utf-8")
    words = len(re.sub(r"```.*?```", "", final, flags=re.S).split())
    code_lines = sum(b.count("\n") for b in re.findall(r"```.*?```", final, flags=re.S))
    pages = words / 380 + code_lines / 48
    print(f"{chapter.name}: {len(outputs)} files, {fails} fails, ~{words} words, ~{code_lines} code lines, ~{pages:.1f} pages")
    for d in chapter.rglob("__pycache__"):
        import shutil; shutil.rmtree(d)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
