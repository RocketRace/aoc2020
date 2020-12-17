from typing import List
import itertools
def solve_naive(data: List[str]):
    first = 0
    # set containing all active cells (x, y, z)
    # because each dimension can be infinite (i.e. lists are inconvenient)
    actives = set()
    actives_4 = set()
    for y, row in enumerate(data):
        for x, bit in enumerate(row):
            if bit == "#":
                actives.add((x, y, 0))
                actives_4.add((x, y, 0, 4))

    deltas_3 = [x for x in itertools.product((0,1,-1), repeat=3) if x != (0,0,0)]
    def get_counts_3(x, y, z):
        count = 0
        for dx, dy, dz in deltas_3:
            new_pos = (x + dx, y + dy, z + dz)
            if new_pos in actives:
                count += 1
        return count
    
    def add_empties(x, y, z, *, empties: set):
        count = 0
        i = 0
        for dx, dy, dz in deltas_3:
            i += 1
            new_pos = (x + dx, y + dy, z + dz)
            if new_pos in actives:
                count += 1
            else:
                empties.add(new_pos)
        return count

    for _ in range(6):
        empties = set()
        remove = set()
        new = set()
        for pos in actives:
            count = add_empties(*pos, empties = empties)
            if count != 2 and count != 3:
                remove.add(pos)
        for pos in empties:
            count = get_counts_3(*pos)
            if count == 3:
                new.add(pos)
        actives.update(new)
        actives.difference_update(remove)

    first = len(actives)

    deltas_4 = [x for x in itertools.product((0,1,-1), repeat=4) if x != (0,0,0,0)]
    def get_counts_4(x, y, z, w):
        count = 0
        for dx, dy, dz, dw in deltas_4:
            new_pos = (x + dx, y + dy, z + dz, w + dw)
            if new_pos in actives_4:
                count += 1
        return count
    
    def add_empties_4(x, y, z, w, *, empties: set):
        count = 0
        i = 0
        for dx, dy, dz, dw in deltas_4:
            i += 1
            new_pos = (x + dx, y + dy, z + dz, w + dw)
            if new_pos in actives_4:
                count += 1
            else:
                empties.add(new_pos)
        return count

    for _ in range(6):
        empties = set()
        remove = set()
        new = set()
        for pos in actives_4:
            count = add_empties_4(*pos, empties = empties)
            if count != 2 and count != 3:
                remove.add(pos)
        for pos in empties:
            count = get_counts_4(*pos)
            if count == 3:
                new.add(pos)
        actives_4.update(new)
        actives_4.difference_update(remove)


    second = len(actives_4)
    return [first, second]

implementations = (solve_naive,)
