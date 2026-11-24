#!/usr/bin/env python3
"""Ship It Friday — print (and write) the one-line commit message.

Reads the entry line from entry.txt next to this file, prints it to
stdout, and writes it to /output/entry.txt for the make.fun harness.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
    line = f.read().strip()

print(line)

try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
except OSError:
    pass
