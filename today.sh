#!/bin/bash

day=$(date +%-d)
touch "days/day$day.txt"
echo "implementations = ()" > "days/day$day.py"