from typing import List
from itertools import combinations
def solve_naive(data: List[str]):
    first = 0
    data = [int(x) for x in data]
    acc = data[:25]
    for i in data[25:]:
        if all(n + m != i for n, m in combinations(acc, 2)):
            first = i
            break
        acc.append(i)
        acc.pop(0)
    second = 0
    for i, n in enumerate(data):
        j = 0
        while True:
            if sum(data[i:i+j]) > first:
                break
            if sum(data[i:i+j]) == first:
                second = min(data[i:i+j]) + max(data[i:i+j])
                return [first, second]
            j += 1
    return [first, second]

implementations = (solve_naive,)
