import math
from typing import List

def solve_naive(data: List[str]):
    first = 0
    instrs = [(x[0], int(x[1:])) for x in data]
    x = y = 0
    dir = 0
    for instr, amount in instrs:
        if instr == "N":
            y -= amount
        elif instr == "S":
            y += amount
        elif instr == "E":
            x += amount
        elif instr == "W":
            x -= amount
        elif instr == "L":
            dir += amount // 90
            dir %= 4
        elif instr == "R":
            dir -= amount // 90
            dir %= 4
        else: # instr == "F"
            if dir == 0:
                x += amount
            elif dir == 1:
                y -= amount
            elif dir == 2:
                x -= amount
            else: # dir == 3
                y +=  amount
    first = abs(x) + abs(y)
    second = 0
    w_x = 10
    w_y = -1
    x = y = 0
    for instr, amount in instrs:
        if instr == "N":
            w_y -= amount
        elif instr == "S":
            w_y += amount
        elif instr == "E":
            w_x += amount
        elif instr == "W":
            w_x -= amount
        elif instr == "L":
            for i in range(amount // 90):
                w_x, w_y =  w_y, -w_x
        elif instr == "R":
            for i in range(amount // 90):
                w_x, w_y =  -w_y, w_x
        else: # instr == "F"
            x += w_x * amount
            y += w_y * amount
    second = abs(x) + abs(y)
    return [first, second]

def s(I):
 f=lambda c:abs(c.real)+abs(c.imag);p=P=0j;d=p+1;w=10-1j;g=[1j,-1j,1]
 for i,*r in I:a=int(''.join(r));x=(g+[-1,0])["SNEW".find(i)]*a;y=g["RL".find(i)]**(a//90);z=a*(i=="F");p+=x+z*d;P+=z*w;w=w*y+x;d*=y
 return f(p),f(P)

implementations = (solve_naive,s)