from typing import List
def solve_naive(data: List[str]):
    ones = zeros = 0
    mem = {}
    for line in data:
        if line.startswith("mask ="):
            mask = line[6:]
            ones = int("".join("1" if x == "1" else "0" for x in mask), base=2)
            zeros = int("".join("1" if x == "0" else "0" for x in mask), base=2)
        else:
            addr = line[4:line.find("]")]
            num = int(line[line.find("=")+2:])
            mem[addr] =( num | ones) & ~ zeros
    first = sum([*mem.values()])
    ones = 0
    positions = []
    mem = {}
    for line in data:
        if line.startswith("mask ="):
            mask = line[6:]
            ones = int("".join("1" if x == "1" else "0" for x in mask), base=2)
            positions = [36 - i for i, x in enumerate(mask) if x == "X"]
        else:
            addr = int(line[4:line.find("]")])
            addr |= ones
            for i in range(1 << len(positions)):
                n = list(bin(addr)[2:].rjust(36, "0"))
                for bit, pos in zip(bin(i)[2:].rjust(len(positions), "0"), positions):
                    n[35-pos] = bit
                mem["".join(reversed(n))] = int(line[line.find("=")+2:])
    second = sum([*mem.values()])
    return [first, second]

implementations = (solve_naive,)
