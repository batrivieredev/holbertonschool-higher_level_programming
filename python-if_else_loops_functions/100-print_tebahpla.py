#!/usr/bin/python3
print("".join(chr(c) if c % 2 == 1 else chr(c - 32) for c in range(122, 96, -1)), end="")
