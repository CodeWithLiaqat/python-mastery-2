# Book build runtime: input() ko terminal jaisa transcript dikhane ke liye patch karta hai.
import builtins
import os
import sys

if os.environ.get("BOOK_ECHO_INPUT"):
    def _input(prompt=""):
        sys.stdout.write(str(prompt))
        sys.stdout.flush()
        line = sys.stdin.readline()
        if not line:
            raise EOFError("EOF when reading a line")
        line = line.rstrip("\n")
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        return line
    builtins.input = _input
