import itertools

def solve_naive(data):
    first = next((data[i]*data[j] for i, j in itertools.combinations(range(len(data)), 2) if data[i]+data[j] == 2020))
    second = next((data[i]*data[j]*data[k] for i, j, k in itertools.combinations(range(len(data)), 3) if data[i]+data[j]+data[k] == 2020))
    return [first, second]

solve = solve_naive