from collections import Counter, defaultdict
from itertools import accumulate, chain
from functools import reduce
from operator import mul, add
import os
import time
import math
import re
import heapq

def main():

    # input
    print(os.getcwd())
    day = "06"
    year = "2025"
    input_file = f"./inputs/day{day}.txt"
    with open(input_file) as f:
        lines = f.read().splitlines()
    # calc
    start_time = time.time()
    part1, part2 = 0, 0
    paramLines =[]
    # print(lines)
    for i in range(len(lines)-1):
        # print(list(map(int,lines[i].split())))
        paramLines.append(list(map(int,lines[i].split())))
    params = []
    for i in range(len(paramLines[0])):
        ps =[]
        for j in range(len(paramLines)):
            ps.append(paramLines[j][i])
        params.append(ps)

    # print(params)
    ops = lines[-1].split()
    # print(ops)
    p1List = []
    for i,p in enumerate(params):
        if ops[i] =='+':
            p1List.append(reduce(add,params[i]))
        else:
            p1List.append(reduce(mul,params[i]))
    print(p1List)
    part1 = sum(p1List)
    # ops = []
    # params = []
    # for i in range(len(lines[0])):
    #     ps = []
    #     for j in range(len(lines)-1):
    #         ps.append(int(lines))


    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
