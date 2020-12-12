import json
from time import time

with open("solutions.json") as fp:
    solutions = json.load(fp)

def check(day):
    with open(f"days/day{day}.txt") as fp:
        data = [x.strip() for x in fp.readlines()]
    with open(f"days/day{day}.py") as fp:
        new_globals = globals().copy()
        exec(fp.read(), new_globals)
        impls = new_globals["implementations"]
        if len(impls) == 1:
            print(f"\033[1mDay {day}: 1 implementation found.\033[0m")
        else:
            print(f"\033[1mDay {day}: {len(impls)} implementations found.\033[0m")
        s_1, s_2 = solutions[day - 1]
        for i, impl in enumerate(impls):
            t = time()
            p_1, p_2 = impl(data)
            dt = time() - t
            count = int(0.5 / (dt + 0.01)) + 1
            total = 0
            for _ in range(count):
                t = time()
                impl(data)
                dt = time() - t
                total += dt
            mean = total / count
            print(f"Implementation {i + 1} took {mean:.3} s:")
            if p_1 == s_1:
                print(f"- Part 1 \033[32;40;1mpassed\033[0m (got {p_1})")
            else:
                print(f"- Part 1 \033[31;40;1mfailed\033[0m (expected {s_1}, got {p_1})")
            if p_2 == s_2:
                print(f"- Part 2 \033[32;40;1mpassed\033[0m (got {p_2})")
            else:
                print(f"- Part 2 \033[31;40;1mfailed\033[0m (expected {s_2}, got {p_2})")

day = input("Day to solve (omit to solve all): ").strip()

if not day:
    try:
        for i in range(25):
            check(i + 1)
    except FileNotFoundError:
        print("No more days found.")
else:
    check(int(day))