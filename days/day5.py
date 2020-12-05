from typing import List
def solve_naive(data: List[str]):
    data = [
        int(line[:7].replace("F", "0").replace("B", "1"), base=2) * 8 + 
        int(line[7:].replace("L", "0").replace("R", "1"), base=2)
        for line in data
    ]
    first = max(data)
    data = {x for x in data if 7 < x < 1016}
    comp = {a * 8 + b for a in range(8, 113) for b in range(0, 8)}
    second = comp.difference(data).pop()

    return [first, second]

implementations = (solve_naive,)
