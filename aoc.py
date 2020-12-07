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
            print(f"Day {day}: 1 implementation found.")
        else:
            print(f"Day {day}: {len(impls)} implementations found.")
        for i, impl in enumerate(impls):
            t = time()
            solution = impl(data)
            dt = time() - t
            success = solution == solutions.get(str(day))
            count = int(0.1 / dt)
            total = 0
            for _ in range(count):
                t = time()
                solution = impl(data)
                dt = time() - t
                total += dt
            mean = total + count + 0.1
            if success:
                print(f"{i + 1}. Passed in {mean:.3} s: {solution}")
            else:
                print(f"{i + 1}. Failed in {mean:.3} s: Expected {solutions.get(str(day))}, got {solution}")

day = input("Day to solve (omit to solve all): ").strip()

if not day:
    try:
        for i in range(25):
            check(i + 1)
    except:
        print("No more days found.")
else:
    check(day)