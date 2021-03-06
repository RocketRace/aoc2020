import itertools
from typing import List
def solve_naive(data: List[str]):
    '''
    1. O(N^2)
    
    2. O(N^3)
    '''
    data = [int(x) for x in data]
    first = next((data[i]*data[j] for i, j in itertools.combinations(range(len(data)), 2) if data[i]+data[j] == 2020))
    second = next((data[i]*data[j]*data[k] for i, j, k in itertools.combinations(range(len(data)), 3) if data[i]+data[j]+data[k] == 2020))
    return [first, second]

def solve_less_naive(data: List[str]):
    '''
    1. O(N)
    
    2. O(N^2)
    '''
    data = [int(x) for x in data]
    non_unique = set(data)
    first = next((n * (2020 - n) for n in data if 2020 - n in non_unique))
    second = next((n * m * (2020 - n - m) for n, m in itertools.combinations(data, 2) if 2020 - n - m in non_unique))
    return [first, second]

def solve_even_less_naive(data: List[str]):
    '''
    1. O(N)
    
    2. O(NlogN)
    '''
    data = [int(x) for x in data]
    non_unique = set(data)
    first = next((n * (2020 - n) for n in data if 2020 - n in non_unique))
    asc = sorted(data)
    def loop():
        for i, n in enumerate(asc):
            for m in asc[i:]:
                if n + m > 2020:
                    break
                if 2020 - n - m in non_unique:
                    return n * m * (2020 - n - m)
    second = loop()
    return [first, second]

implementations = (solve_naive, solve_less_naive, solve_even_less_naive)