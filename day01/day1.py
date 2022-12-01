#!/usr/bin/env python
# Clear the terminal
print("\033[2J\033[H") # ]]

# Grid, Direction
# Direction.NORTH,SOUTH,EAST,WEST,NE,SE,NW,SW
# g = Grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# g.width, g.height, (y, x) in g (coords), g[(y, x)], g[(y, x)] = 5
# for item in g => iterate over items in row major order
# g.row_major(_with_index)() => iterate over items in row major order
# g.column_major(_with_index)() => iterate over items in column major order
# g.apply(func) => call func with each item
# g.map(func) => return new Grid with results of func
# g.ray_from((y, x), direction), yields items from a starting point in a direction
# g.around(_with_index) => What it sounds like

# Graph
# g = Graph()
# g.add_edge(from, to, weight=something)
# g.dijkstra(start) => Dijkstra (has `distance_to`, and `path_to` methods)

# ShuntingYard
# Expression parser with configurable precedence for operations so you can throw out (B)EDMAS (no support for brackets)
from aoc_utils import * # type: ignore

from aocd import get_data, submit


data = get_data(year=2022, day=1, block=True)
lines = data.split("\n\n")
max = []
for i, elf in enumerate(lines):
    cals = sum(int(n) for n in elf.split("\n"))
    max.append(cals)

print(sum(sorted(max)[-3:]))


# submit(answer, part="a", day=1, year=2022)
