#!/usr/bin/env python
# Clear the terminal
print("\033[2J\033[H") # ]]

from aoc_utils import * # type: ignore

from aocd import get_data, submit


data = get_data(year=2022, day=1, block=True)
elves = data.split("\n\n")
calories = [sum(int(n) for n in elf.split("\n")) for elf in elves]
print(sum(sorted(calories)[-3:]))


# submit(answer, part="a", day=1, year=2022)
