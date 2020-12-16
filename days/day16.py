from typing import List

def solve_naive(data: List[str]):
    first = 0
    state = 0
    checks = {}
    you = None
    valids = []
    for row in data:
        if row == "":
            state += 1
        elif row.endswith(":"):
            continue
        else:
            if state == 2:
                nums = list(map(int, row.split(",")))
                valid = True
                for n in nums:
                    for c_a, c_b in checks.values():
                        if n in c_a or n in c_b:
                            break
                    else:
                        first += n
                        valid = False
                if valid:
                    # I would have made a new copy of the generator in case the list doesn't need to be
                    # evaluated all the way, but it turns out that's not the case
                    valids.append(nums)
            elif state == 1:
                you = map(int, row.split(","))
            else:
                field, ranges = row.split(": ")
                range_a, range_b = ranges.split(" or ")
                a_start, a_end = map(int, range_a.split("-"))
                b_start, b_end = map(int, range_b.split("-"))
                # Each field requirement is a union of two (inclusive) range checks
                checks[field] = (range(a_start, a_end + 1), range(b_start, b_end + 1))
    field_names = set(checks)
    field_options = [] 
    for valid in zip(*valids): # I like this zip
        options = field_names.copy()
        for num in valid:
            for option, (check_a, check_b) in checks.items():
                if option not in options:
                    continue        
                if num not in check_a and num not in check_b:
                    options.remove(option)
        field_options.append(options)
    
    fields = {}
    while len(fields) < len(field_names):
        for i, options in enumerate(field_options):
            # remove the field from the rest of the field options if it's certain
            if len(options) == 1:
                final = options.pop() 
                fields[i] = final
                for combed in field_options:
                    combed.discard(final)            
    
    second = 1
    for i, num in enumerate(you):
        # should be 6 values
        if fields[i].startswith("departure"):
            second *= num
    
    return first, second

implementations = (solve_naive,)