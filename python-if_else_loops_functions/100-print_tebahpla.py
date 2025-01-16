#!/usr/bin/python3
print("".join(chr(c - (c % 2) * 32) for c in range(122, 96, -1)), end="")
