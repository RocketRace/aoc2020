from typing import List
def solve_naive(data: List[str]):
    first = 0
    aa = [x.split(" ") for x in data]
    traversed = set()
    acc = 0
    pc = 0
    while True:
        if pc in traversed:
            first = acc
            break
        traversed.add(pc)
        op, t = aa[pc]
        if op == "jmp":
            pc = pc + int(t)
        elif op == "acc":
            pc += 1
            acc += int(t)
        else:
            pc += 1
    second = 0
    for i in range(len(data)):
        acc = 0
        pc = 0
        traversed = set()
        try:
            while True:
                if pc in traversed:
                    break
                op, t = aa[pc]
                if pc == i and op == "jmp":
                    op = "nop"
                elif pc == i and op == "nop":
                    op = "jmp"
                if op == "jmp":
                    traversed.add(pc)
                    pc = pc + int(t)
                elif op == "acc":
                    acc += int(t)
                    pc += 1
                else:
                    pc += 1
        except IndexError:
            second = acc
            break
    return [first, second]

implementations = (solve_naive,)
