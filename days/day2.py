from typing import List
def solve_naive(data: List[str]):
    '''
    1. O(Scans through whole string twice, with C bindings)

    2. O(Scans through whole string once, with C bindings)
    '''
    first = 0
    for entry in data:
        rule, x, password = entry.split(" ")
        char = x[0]
        n, m = (int(x) for x in rule.split("-"))
        if n <= password.count(char) <= m:
            first += 1
    second = 0
    for entry in data:
        rule, x, password = entry.split(" ")
        char = x[0]
        n, m = (int(x) for x in rule.split("-"))
        if (password[n - 1] == char) ^ (password[m - 1] == char):
            second += 1
    return [first, second]

implementations = (solve_naive,)