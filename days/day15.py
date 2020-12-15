from collections import Counter
from typing import List
def solve_naive(data: List[str]):
    first = 0
    history = [int(x) for x in data[0].split(",")]
    counts = Counter(history)
    last = counts[-1]
    def find_last_2(hist, num):
        last = -1
        second_last = -1
        for i, n in enumerate(hist):
            if n == num:
                if i > last:
                    second_last = last
                    last = i
        if second_last == -1:
            return 0
        return last - second_last
    for _ in range(2020 - len(history)):
        if last in counts:
            last = find_last_2(history, last)
        else:
            last = 0
        history.append(last)
        counts[last] += 1
    first = last
    history = [int(x) for x in data[0].split(",")]
    checks = {n: i for i,n in enumerate(history)}
    for  i in range(len(history) - 1, 30000000):
        history.append(i - checks.get(history[i], i))
        checks[history[i]] = i

    second = history[-2]
    return [first, second]

implementations = (solve_naive,)
