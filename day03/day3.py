#!/usr/bin/env python

from aoc_utils import * # type: ignore

from aocd import get_data

data = get_data(year=2022, day=3, block=True)
lines = data.splitlines()

t = 0

for i in range(0, len(lines), 3):
    a, b, c = lines[i], lines[i+1], lines[i+2]
    sa, sb, sc = set(a), set(b), set(c)

    common = list(sa.intersection(b).intersection(sc))[0]
    if common.islower():
        prior = ord(common) - ord('a') + 1
    else:
        prior = ord(common) - ord('A') + 27
    t += prior

print(t)
