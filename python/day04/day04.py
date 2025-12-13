from collections import Counter, defaultdict
from itertools import accumulate, chain
import os
import time
import math
import re
import heapq

def nb(pos):
    x,y = pos
    return [(x-1,y-1), (x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1), (x+1,y), (x+1,y+1)]
def main():

    # input
    print(os.getcwd())
    day = "04d"
    year = "2025"
    input_file = f"./inputs/day{day}.txt"

    part1, part2 = 0, 0
    floorMap = set()
    d = {'@':1, '.':0}
    # calc
    start_time = time.time()
    with open(input_file) as f:
        lines = f.read().splitlines()
    # print(lines)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c=='@':
                floorMap[(x,y)] = 1

    # output
    # print(floorMap)
    # part1
    for tile in floorMap:
        x,y = tile
        ns = nb((x,y))
        # print(ns)
        tmpSum = 0
        for n in ns:
            print(floorMap.get(n))

    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
