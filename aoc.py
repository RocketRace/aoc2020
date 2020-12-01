import json

with open("solutions.json") as fp:
    solutions = json.load(fp)

def check(day):
    with open(f"days/day{day}.txt") as fp:
        data = [int(x.strip()) for x in fp.readlines()]
    with open(f"days/day{day}.py") as fp:
        new_globals = globals().copy()
        exec(fp.read(), new_globals)
        solution = new_globals['solve'](data)
        if solution == solutions[str(day)]:
            print(f"Day {day}: Passed [{solution}]")
        else:
            print(f"Day {day} failed: Expected {solutions[str(day)]}, got {solution}")

day = input("Day to solve: ").strip()

if not day:
    for i in range(25):
        check(i + 1)
else:
    check(day)