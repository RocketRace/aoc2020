#!/bin/bash

day=$(date +%-d)
touch "days/day$day.txt"
echo "implementations = ()" > "days/day$day.py"
code "days/day$day.txt"
code "days/day$day.py"