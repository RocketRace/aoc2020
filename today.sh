#!/bin/bash

day=$(date +%-d)
touch "days/day$day.txt"
echo "from typing import List
def solve_naive(data: List[str]):
    first = 0
    second = 0
    return [first, second]

implementations = (solve_naive,)" > "days/day$day.py"
code solutions.json
code "days/day$day.txt"
code "days/day$day.py"