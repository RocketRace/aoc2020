import itertools
from typing import List
def solve_naive(data: List[str]):
    first = 0
    width = len(data[0])
    i = 0
    for row in data[1:]:
        i += 3
        if row[i % width] == "#":
            first += 1
    second = 0
    i=j=k=l=m = 0
    acc = [0,0,0,0,0]
    for row in data[1:]:
        i += 1
        j += 3
        k += 5
        l += 7
        if row[i % width] == "#":
            acc[0] += 1
        if row[j % width] == "#":
            acc[1] += 1
        if row[k % width] == "#":
            acc[2] += 1
        if row[l % width] == "#":
            acc[3] += 1
        if i % 2 == 0:
            m += 1
            if row[m % width] == "#":
                acc[4] += 1
    second = acc[0] * acc[1] * acc[2] * acc[3] * acc[4]
    return [first, second]

implementations = (solve_naive,)
