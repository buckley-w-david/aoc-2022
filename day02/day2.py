#!/usr/bin/env python

from aocd import get_data


data = get_data(year=2022, day=2, block=True)
lines = data.splitlines()

ROCKA = "A"
PAPERA = "B"
SCIA = "C"

ROCKB = LOSE = "X"
PAPERB = TIE = "Y"
SCIB = WIN = "Z"

rules = {
    ROCKA: {
        ROCKB: 4,
        PAPERB: 8,
        SCIB: 3,
    },
    PAPERA: {
        ROCKB: 1,
        PAPERB: 5,
        SCIB: 9,
    },
    SCIA: {
        ROCKB: 7,
        PAPERB: 2,
        SCIB: 6,
    }
}

total = 0

for line in lines:
    a, b = line.split()
    if a == ROCKA:
        if b == LOSE:
            choice = SCIB
        elif b == TIE:
            choice = ROCKB
        elif b == WIN:
            choice = PAPERB
    elif a == PAPERA:
        if b == LOSE:
            choice = ROCKB
        elif b == TIE:
            choice = PAPERB
        elif b == WIN:
            choice = SCIB
    elif a == SCIA:
        if b == LOSE:
            choice = PAPERB
        elif b == TIE:
            choice = SCIB
        elif b == WIN:
            choice = ROCKB
    total += rules[a][choice]
    
print(total)
    


# submit(answer, part="a", day=2, year=2022)
