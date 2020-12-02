def solve_naive(data): # O(Scans through whole string twice), O(Scans through whole string almost twice)
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

def solve_faster(data):
    first = 0

implementations = (solve_naive,)