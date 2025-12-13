from collections import Counter
from itertools import accumulate, chain
import os
import time
import math
import re
import heapq

def calcLine1(line):
    n =  len(line)
    intLine = [int(i) for i in line]
    leftMax = [max(intLine[:i]) for i in range(1,n)]
    rightMax = [max(intLine[i:]) for i in range(n-1,0,-1)]
    # print(leftMax,rightMax)
    return max([10*leftMax[i] + rightMax[n-2-i] for i in range(n-1)])

def calcLine2(line):
    n = len(line)
    result=[]
    for i, d in enumerate(line):
        while result and result[-1] < d and len(result) + (n-i) >12:
            result.pop()
        if len(result) < 12:
            result.append(d)
    return int("".join(result[:12]))

def main():

    # input
    print(os.getcwd())
    day = "03"
    year = "2025"
    input_file = f"./inputs/day{day}.txt"

    part1, part2 = 0, 0

    # calc
    start_time = time.time()
    with open(input_file) as f:
        lines = f.read().splitlines()
    print(lines)
    part1 = sum(map(calcLine1,lines))
    part2 = sum(map(calcLine2,lines))

    # output
   
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
