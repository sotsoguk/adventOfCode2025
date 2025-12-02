from collections import Counter
from itertools import accumulate, chain
import os
import time
import math
import re
import heapq


def main():

    # input
    print(os.getcwd())
    day = "02"
    year = "2025"
    input_file = f"./inputs/day{day}.txt"

    part1, part2 = 0, 0

    # calc
    start_time = time.time()
    with open(input_file) as f:
        lines = f.read().splitlines()

    regex1 = re.compile(r"^(\w+)\1{1}$")
    regex2 = re.compile(r"^(\w+)\1+$")

    idList = list(
        chain(
            *list(
                map(str, i)
                for i in (
                    range(int(x[0]), int(x[1]) + 1)
                    for x in (x.split("-") for x in lines[0].split(","))
                )
            )
        )
    )

    part1 = sum(map(int, [i for i in idList if regex1.match(i)]))
    part2 = sum(map(int, [i for i in idList if regex2.match(i)]))

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
