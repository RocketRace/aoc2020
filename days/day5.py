from typing import List
def solve_naive(data: List[str]):
    data = [
        int(line[:7].replace("F", "0").replace("B", "1"), base=2) * 8 + 
        int(line[7:].replace("L", "0").replace("R", "1"), base=2)
        for line in data
    ]
    first = max(data)
    data = {x for x in data if 7 < x < 1016} # Uh oh read the question wrong
    comp = {a * 8 + b for a in range(8, 113) for b in range(0, 8)} # uh oh hardcoded
    second = comp.difference(data).pop()

    return [first, second]

def solve_less_naive(data: List[str]):
    data = [
        int(x.replace("F","0").replace("L","0").replace("B","1").replace("R","1"), base=2)
        for x in data
    ]
    first = max(data)
    second = 0
    comp = set(data)
    for i in range(min(data), first + 1):
        if i not in comp:
            second = i
            break

    return [first, second]

implementations = (solve_naive, solve_less_naive,)
