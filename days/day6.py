from typing import List
def solve_naive(data: List[str]):
    first = 0
    acc = set()
    for line in data:
        if line == "":
            first += len(acc)
            acc = set()
        else:
            acc.update(line)
    first += len(acc)
    second = 0
    acc = set()
    b = True
    for line in data:
        if b: 
            acc = set(line)
            b = False
        elif line == "":
            second += len(acc)
            acc = set()
            b = True
        else:
            acc = {x for x in line if x in acc}
    second += len(acc)
    return [first, second]

implementations = (solve_naive,)
