import functools
import operator
from typing import List
def solve_naive(data: List[str]):
    data = {int(x) for x in data}
    acc = 0
    one = 0
    three = 0
    while True:
        if acc + 1 in data:
            acc = acc + 1
            one += 1
        elif acc + 2 in data:
            acc = acc + 2
        elif acc + 3 in data:
            acc = acc + 3
            three += 1
        else:
            three += 1
            break
    first = one * three
    acc = 0
    s = {}
    def check(a):
        if max(data) <= a:
            return 1
        x = 0
        if a + 1 in data:
            s[a + 1] = s.get(a + 1) if s.get(a + 1) is not None else check(a + 1)
            x += s[a + 1]
        if a + 2 in data:
            s[a + 2] = s.get(a + 2) if s.get(a + 2) is not None else check(a + 2)
            x += s[a + 2]
        if a + 3 in data:
            s[a + 3] = s.get(a + 3) if s.get(a + 3) is not None else check(a + 3)
            x += s[a + 3]
        return x
    second = check(0)
    return [first, second]

implementations = (solve_naive,)
