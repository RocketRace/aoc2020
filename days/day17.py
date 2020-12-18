from typing import List
import itertools
def solve_naive(data: List[str]):
    # set containing all active cells (x, y, z)
    # because each dimension can be infinite (i.e. lists are inconvenient)
    actives_3d = set()
    actives_4d = set()
    actives_10d = set()
    for y, row in enumerate(data):
        for x, bit in enumerate(row):
            if bit == "#":
                actives_3d.add((x, y, 0))
                actives_4d.add((x, y, 0, 0))
                actives_10d.add((x, y, 0, 0, 0, 0, 0, 0, 0, 0))

    def solve_dimensions(initial, *, n, t):
        actives = initial
        zero = tuple([0 for _ in range(n)])
        deltas = [x for x in itertools.product((0, 1, -1), repeat=n) if x != zero]
        
        if n == 3:
            def get_counts(pos):
                count = 0
                x, y, z = pos
                for dx, dy, dz in deltas:
                    new_pos = (x + dx, y + dy, z + dz)
                    if new_pos in actives:
                        count += 1
                return count
        elif n == 4:
            def get_counts(pos):
                count = 0
                x, y, z, w = pos
                for dx, dy, dz, dw in deltas:
                    new_pos = (x + dx, y + dy, z + dz, w + dw)
                    if new_pos in actives:
                        count += 1
                return count
        else:
            def get_counts(pos):
                count = 0
                for delta_pos in deltas:
                    new_pos = tuple([x + y for x, y in zip(pos, delta_pos)])
                    if new_pos in actives:
                        count += 1
                return count
        if n == 3:
            def add_empties(pos, empties):
                count = 0
                x, y, z = pos
                for dx, dy, dz in deltas:
                    new_pos = (x + dx, y + dy, z + dz)
                    if new_pos in actives:
                        count += 1
                    else:
                        empties.add(new_pos)
                return count
        elif n == 4:
            def add_empties(pos, empties):
                count = 0
                x, y, z, w = pos
                for dx, dy, dz, dw in deltas:
                    new_pos = (x + dx, y + dy, z + dz, w + dw)
                    if new_pos in actives:
                        count += 1
                    else:
                        empties.add(new_pos)
                return count
        else:
            def add_empties(pos, empties):
                count = 0
                for delta_pos in deltas:
                    new_pos = tuple([x + y for x, y in zip(pos, delta_pos)])
                    if new_pos in actives:
                        count += 1
                    else:
                        empties.add(new_pos)
                return count

        for _ in range(t):
            empties = set()
            remove = set()
            new = set()
            for pos in actives:
                count = add_empties(pos, empties)
                if count != 2 and count != 3:
                    remove.add(pos)
            for pos in empties:
                count = get_counts(pos)
                if count == 3:
                    new.add(pos)
            actives |= new
            actives -= remove
        
        return len(actives)

    first = solve_dimensions(actives_3d, n=3, t=6)
    second = solve_dimensions(actives_4d, n=4, t=6)
    return [first, second]

implementations = (solve_naive,)
