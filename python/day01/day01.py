from collections import Counter
from itertools import accumulate
import os
import time
import math
import heapq

def sign(x):
    if x > 0:
        return 1
    elif x<0: 
        return -1
    return 0

def main():

    # input
    print(os.getcwd())
    day = "01d"
    year = "2025"
    input_file = f"./inputs/day{day}.txt"
    # print(input_file)
    part1, part2 = 0, 0
    # leftList, rightList = [], []

    with open(input_file) as f:
        # groups = f.read().split('\n')
        lines = f.read().splitlines()
    
    dirs = {'R': 1, 'L': -1}
    # dirs = {'R': 1, 'L': -1}
    # intLines1 = list(map(lambda x: dirs[x[0]] * int(x[1:]), lines))
    # intLines2 = list(map(list(lambda x: [dirs[x[0]] * int(x[1:])]),lines))

    # p1 = lambda x: dirs[x[0]] * int(x[1:])
    lines1 = []
    lines2 = []
    for l in lines:
        lines1 += [dirs[l[0]] *int(l[1:])]
        lines2 += [dirs[l[0]]] * int(l[1:])
    print(lines1)
    print(lines2)
    # intLines = []
    # for l in lines:
    #     num =0
    #     if l[0] == 'R':
    #         num = int(l[1:])
    #     else:
    #         num = -int(l[1:])
    #     intLines.append(num)
    
    # # print(intLines)
    # positions = [50]
    # for i in intLines:
    #     positions.append((positions[-1] + i) % 100)
    # # print(positions)
    # cnt = Counter(positions)
    # # print(cnt[0])    

    # # part 2
    # pos = 50
    # for i in intLines:
      
    #     pos = pos +i
    #     a,b = divmod(pos,100)
    #     # if (pos<0 and b==0):
    #     #     part2 += 1
    #     if i<0:
    #         a += 1
    #     part2 +=abs(a)
        
    #     print(pos,i,a,b,part2,pos%100)
    #     pos = pos % 100
    #     if pos ==0 and i<0:
    #         part2 +=1
    #     # if (pos==0 and b==0):
    #     #     part2 += 1

    #     # s = sign(i)
    #     # a = abs(i)
    #     # x,y = divmod(a,100)
    #     # part2 += x
    #     # # y = s * y
    #     # # pos += y
    #     # # if ((y!= 0) and (pos <= 0 or pos > 100)):
    #     # #     part2 += 1
        # if y>0:
        #     if s >0:
        #         if pos + y > 100:
        #             part2 += 1
        #     else:
        #         if pos -y <= 0:
        #             part2 += 1
        # elif y==0:
        #     if pos == 0:
        #         part2 +=1 
        # pos = (pos+s*y) % 100

        # pos += i
        # if (pos >= 0):
        #     part2 += pos // 100
        # elif (pos<0):
        #     part2 += (abs(pos)// 100) +1
        # pos = abs(pos) % 100
        # for j in range(abs(i)):
        #     pos = (pos + sign(i)) %100
        #     # print(pos)
        #     if (pos ==0):
        #         part2 += 1
        # else:
        #     for j in range(abs(i)):
        #         pos = (pos -1) % 100
        #         if (pos ==0):
        #             part2 += 1
        # if (i>0):
        #     if i >(100-pos):
        #         part2 += 1
        #     rem = i - (100-pos)
        #     if (rem >0):
        #         part2 += (rem // 100)
        #     pos = (pos + i) % 100
        # else:
        #     if abs(i) >= (pos):
        #         part2 += 1
        #     rem = i + pos
        #     part2 += (abs(rem) // 100)
        #     pos = (pos +i) % 100
        # if (pos == 0):
        #     part2 += 0
   
        # print(i, pos, part2, rem)
    print(part2)     
    # for l in lines:
    #     a, b = list(map(int, l.split("   ")))
    #     leftList.append(a)
    #     rightList.append(b)

    # counterLeft, counterRight = Counter(leftList), Counter(rightList)

    # # calc
    # start_time = time.time()
    # part1 = sum(
    #     map(
    #         lambda tuple: abs(tuple[0] - tuple[1]),
    #         zip(sorted(leftList), sorted(rightList)),
    #     )
    # )

    # part2 = sum([counterLeft[el] * el * counterRight[el] for el in counterLeft])

    # # output
    # duration = int((time.time() - start_time) * 1000000)
    # header = "#" * 20
    # print(
    #     f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    # )



if __name__ == "__main__":
    main()