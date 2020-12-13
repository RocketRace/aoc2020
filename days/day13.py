from typing import List
import sympy
def solve_naive(data: List[str]):
    first = 0
    earliest, raw_buses = data
    earliest = int(earliest)
    buses = [int(y) for y in raw_buses.split(",") if y != "x"]
    offsets = [(bus, bus - earliest % bus) for bus in buses]
    time = min(offsets, key=lambda x: x[1])
    first = time[0]*time[1]

    wacky = [(i, int(x)) for i, x in enumerate(raw_buses.split(",")) if x != "x"]
    prod = 1
    n_s = []
    a_s = []
    for i, x in wacky:
        a_s.append(x - i)
        n_s.append(x)
        prod *= x

    def crt(n_s, a_s):
        return sum(
            a * prod // n * pow(prod // n, -1, n)
            for n, a in zip(n_s, a_s)
        ) % prod

    second = crt(n_s, a_s)
    return [first, second]

implementations = (solve_naive,)
