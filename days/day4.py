def solve_naive(data):
    first = 0
    
    comp = {"ecl","pid","eyr","hcl","byr","iyr","hgt"}
    acc = set()
    for line in data:
        if line == "":
            if comp.issubset(acc):
                first += 1
            acc = set()
        else:
            parts = line.split(" ")
            for part in parts:
                acc.add(part.split(":")[0])
    if comp.issubset(acc):
        first += 1
    
    comp = {"ecl","pid","eyr","hcl","byr","iyr","hgt"}
    def check(a):
        if not comp.issubset(acc.keys()):
            return False
        try:
            return all([
                1920 <= int(a["byr"]) <= 2002,
                2010 <= int(a["iyr"]) <= 2020,
                2020 <= int(a["eyr"]) <= 2030,
                (150 <= int(a["hgt"][:-2]) <= 193) if a["hgt"].endswith("cm") else (59 <= int(a["hgt"][:-2]) <= 76),
                a["hcl"].startswith("#") and 0 <= int(a["hcl"][1:], base=16) <= 16_777_215 and len(a["hcl"]) == 7,
                a["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
                len(a["pid"]) == 9 and a["pid"].isnumeric()
            ])
        except: return False

    second = 0
    acc = {}
    for line in data:
        if line == "":
            if check(acc):
                second += 1
            acc = {}
        else:
            parts = line.split(" ")
            for part in parts:
                a,b = part.split(":")
                acc[a] = b 
    if check(acc):
        second += 1

    return [first, second]


implementations = (solve_naive,)
