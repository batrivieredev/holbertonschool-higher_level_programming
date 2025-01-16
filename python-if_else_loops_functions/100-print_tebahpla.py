#!/usr/bin/python3
print("".join(chr(c - 32) if c % 2 else chr(c) for c in range(122, 96, -1)), end="")
