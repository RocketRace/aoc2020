from typing import List
import regex
from regex.regex import sub
def solve_naive(data: List[str]):
    first = second = 0
    patterns = {}
    tests = False
    pattern = pattern_p2 = None
    special_patterns = {
        "8": ["42", "|", "42", "8"],
        "11": ["42", "31", "|", "42", "11", "31"],
    }
    
    def substitute(key):
        ptrn = patterns[key]
        if ptrn[0] in "ab":
            return f"{ptrn[0]}"
        else:
            return f"({''.join('|' if x == '|' else substitute(x) for x in ptrn)})"

    first_instance = {"8": True, "11": True}
    def substitute_pt2(key):
        if key in ("8", "11"):
            ptrn = special_patterns[key]
        else:
            ptrn = patterns[key]
        if ptrn[0] in "ab":
            return f"{ptrn[0]}"
        else:
            nonlocal first_instance
            final = []
            for x in ptrn:
                if x in ("8", "11"):
                    if first_instance[x]:
                        first_instance[x] = False
                        final.append(f"(?<r_{x}>{substitute_pt2(x)})")
                    else:
                        final.append(f"(?&r_{x})")
                elif x == "|":
                    final.append("|")
                else:
                    final.append(f"({substitute_pt2(x)})")
            return "".join(final)

    for line in data:
        if line == "":
            pattern = regex.compile(f"^{substitute('0')}$")
            print(f"^{substitute_pt2('0')}$")
            first_instance = {"8": True, "11": True}
            pattern_p2 = regex.compile(f"^{substitute_pt2('0')}$")
            tests = True
            continue
        if tests:
            if pattern.match(line):
                first += 1
            if pattern_p2.match(line):
                second += 1
        else:
            tokens = line.split(" ")
            key = tokens[0][:-1]
            patterns[key] = [x[1:-1] if x in ('"a"', '"b"') else x for x in tokens[1:]]

    return [first, second]

implementations = (solve_naive,)
