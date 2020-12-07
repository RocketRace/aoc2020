from typing import List
def solve_naive(data: List[str]):
    first = 0
    acc = {}
    for line in data:
        parts = line.split("contain")
        first = parts[0].strip()[:-5]
        if "other" in parts[1]:
            acc[first] = []
            continue
        contains = parts[1].split(",")
        acc[first] = []
        for c in contains:
            acc[first].append((int(c.strip()[0]), " ".join(c.split(" ")[2:-1]).strip()))
    def rec(n):
        if any(["shiny gold" in x[1] for x in acc[n]]):
            return True
        return any([
            rec(x[1]) for x in acc[n]
        ])
    
    first = 0
    for x in acc:
        first += rec(x)

    second = 0
    def recu(n):
        return 1 + sum([
            x[0] * recu(x[1]) for x in acc[n]
        ])
    second = recu("shiny gold") - 1

    return [first, second]

implementations = (solve_naive,)
