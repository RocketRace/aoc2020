from typing import List
def solve_naive(data: List[str]):
    first = 0
    old = [[y for y in x] for x in data]
    while True:
        new = []
        for y, row in enumerate(old):
            new.append([])
            for x, cell in enumerate(row):
                if cell == ".":
                    new[y].append(".")
                elif cell == "L":
                    check = False
                    if y > 0:
                        if old[y-1][x] == "#": check = True
                    if y < len(old) - 1:
                        if old[y+1][x] == "#": check = True
                    if y > 0 and x < len(row) - 1:
                        if old[y-1][x+1] == "#": check = True
                    if y < len(old) - 1 and x < len(row) - 1:
                        if old[y+1][x+1] == "#": check = True
                    if y > 0 and x > 0:
                        if old[y-1][x-1] == "#": check = True
                    if y < len(old) - 1 and x > 0:
                        if old[y+1][x-1] == "#": check = True
                    if x < len(row) - 1:
                        if old[y][x+1] == "#": check = True
                    if x > 0:
                        if old[y][x-1] == "#": check = True
                    if check:
                        new[y].append("L")
                    else:
                        new[y].append("#")
                else:
                    count = 0
                    if y > 0:
                        if old[y-1][x] == "#": count += 1
                    if y < len(old) - 1:
                        if old[y+1][x] == "#": count += 1
                    if y > 0 and x < len(row) - 1:
                        if old[y-1][x+1] == "#": count += 1
                    if y < len(old) - 1 and x < len(row) - 1:
                        if old[y+1][x+1] == "#": count += 1
                    if y > 0 and x > 0:
                        if old[y-1][x-1] == "#": count += 1
                    if y < len(old) - 1 and x > 0:
                        if old[y+1][x-1] == "#": count += 1
                    if x < len(row) - 1:
                        if old[y][x+1] == "#": count += 1
                    if x > 0:
                        if old[y][x-1] == "#": count += 1
                    if count >= 4:
                        new[y].append("L")
                    else:
                        new[y].append("#")
        if new == old:
            break
        old = [x for x in new]
    first = sum(len([x for x in r if x == "#"]) for r in new)
    old = [[y for y in r] for r in data]
    while True:
        new = []
        for y, row in enumerate(old):
            new.append([])
            for x, cell in enumerate(row):
                if cell == ".":
                    new[y].append(".")
                elif cell == "L":
                    check = False
                    if y > 0:
                        m = 1
                        while True:
                            if y - m < 0: break
                            if old[y - m][x] == ".":
                                m += 1
                                continue
                            if old[y-m][x] == "#":
                                check = True
                            break 
                    
                    if y < len(old) - 1:
                        m = 1
                        while True:
                            if m + y > len(old) - 1: break
                            if old[y + m][x] == ".":
                                m += 1
                                continue
                            if old[y+m][x] == "#":
                                check = True
                            break 
                    
                    if y > 0 and x < len(row) - 1:
                        m = 1
                        while True:
                            if m + x > len(row) - 1: break
                            if y - m < 0: break
                            if old[y-m][x+m] == ".":
                                m += 1
                                continue
                            if old[y-m][x+m] == "#":
                                check = True
                            break 
                    
                    if y < len(old) - 1 and x < len(row) - 1:
                        m = 1
                        while True:
                            if m + y > len(old) - 1: break
                            if m + x > len(row) - 1: break
                            if old[y+m][x+m] == ".":
                                m += 1
                                continue
                            if old[y+m][x+m] == "#":
                                

                                check = True
                            break 
                    
                    if y > 0 and x > 0:
                        m = 1
                        while True:
                            if y - m < 0: break
                            if x - m < 0: break
                            if old[y-m][x-m] == ".":
                                m += 1
                                continue
                            if old[y-m][x-m] == "#":
                                check = True
                            break 
                    
                    if y < len(old) - 1 and x > 0:
                        m = 1
                        while True:
                            if m + y > len(old) - 1: break
                            if x - m < 0: break
                            if old[y+m][x-m] == ".":
                                m += 1
                                continue
                            if old[y+m][x-m] == "#":
                                check = True
                            break 
                    
                    if x < len(row) - 1:
                        m = 1
                        while True:
                            if m + x > len(row) - 1: break
                            if old[y][x+m] == ".":
                                m += 1
                                continue
                            if old[y][x+m] == "#":
                                check = True
                            break 
                    
                    if x > 0:
                        m = 1
                        while True:
                            if x - m < 0: break
                            if old[y][x-m] == ".":
                                m += 1
                                continue
                            if old[y][x-m] == "#":
                                check = True
                            break 
                    
                    if check:
                        new[y].append("L")
                    else:
                        new[y].append("#")
                else:
                    count = 0
                    if y > 0:
                        m = 1
                        while True:
                            if y - m < 0: break
                            if old[y - m][x] == ".":
                                m += 1
                                continue
                            if old[y-m][x] == "#":
                                count += 1
                            break 


                    if y < len(old) - 1:
                        m = 1
                        while True:
                            if m + y > len(old) - 1: break
                            if old[y +m][x] == ".":
                                m += 1
                                continue
                            if old[y+m][x] == "#":
                                count += 1
                            break 


                    if y > 0 and x < len(row) - 1:
                        m = 1
                        while True:
                            if m + x > len(row) - 1: break
                            if y - m < 0: break
                            if old[y-m][x+m] == ".":
                                m += 1
                                continue
                            if old[y-m][x+m] == "#":
                                count += 1
                            break 


                    if y < len(old) - 1 and x < len(row) - 1:
                        m = 1
                        while True:
                            if m + y > len(old) - 1: break
                            if m + x > len(row) - 1: break
                            if old[y+m][x+m] == ".":
                                m += 1
                                continue
                            if old[y+m][x+m] == "#":
                                count += 1
                            break 


                    if y > 0 and x > 0:
                        m = 1
                        while True:
                            if y - m < 0: break
                            if x - m < 0: break
                            if old[y-m][x-m] == ".":
                                m += 1
                                continue
                            if old[y-m][x-m] == "#":
                                count += 1
                            break


                    if y < len(old) - 1 and x > 0:
                        m = 1
                        while True:
                            if m + y > len(old) - 1: break
                            if x - m < 0: break
                            if old[y+m][x-m] == ".":
                                m += 1
                                continue
                            if old[y+m][x-m] == "#":
                                count += 1
                            break 


                    if x < len(row) - 1:
                        m = 1
                        while True:
                            if m + x > len(row) - 1: break
                            if old[y][x+m] == ".":
                                m += 1
                                continue
                            if old[y][x+m] == "#":
                                count += 1
                            break 


                    if x > 0:
                        m = 1
                        while True:
                            if x - m < 0: break
                            if old[y][x-m] == ".":
                                m += 1
                                continue
                            if old[y][x-m] == "#":
                                count += 1
                            break 

                    if count >= 5:
                        new[y].append("L")
                    else:
                        new[y].append("#")
        if new == old:
            break
        old = [x for x in new]
    second = sum(len([x for x in r if x == "#"]) for r in new)
    return [first, second]
implementations = (solve_naive,)
