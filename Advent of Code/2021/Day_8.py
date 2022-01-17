import re
import math
import time


class Solution:
    def solution(self, input):
        nums = 0
        with open(f"{input}") as f:
            lines = list(f.readlines())
            for line in lines:
                line = line.split('|')
                nums += len(list(filter(lambda x: x in [2, 3, 4, 7], map(len, line[1].split()))))

        return nums

    def solution_part2(self, input):
        total = 0
        with open(f"{input}") as f:
            lines = list(f.readlines())
            for line in lines:
                d = {}
                line = line.split('|')
                line0 = line[0].split()
                line0.sort(key=len)
                d[1] = set(line0[0])
                d[7] = set(line0[1])
                d[4] = set(line0[2])
                d[8] = set(line0[-1])
                for itm in line0[6:9]:
                    if not ((d[7] | d[4]) - set(itm)):
                        d[9] = set(itm)
                    elif d[1] - set(itm):
                        d[6] = set(itm)
                    elif not (d[1] - set(itm)):
                        d[0] = set(itm)
                for itm in line0[3:6]:
                    if not (d[1] - set(itm)):
                        d[3] = set(itm)
                    elif len(d[4] - set(itm)) == 2:
                        d[2] = set(itm)
                    else:
                        d[5] = set(itm)
                line1 = line[1].split()
                vals = ''
                for itm in line1:
                    for key in d:
                        if d[key] == set(itm):
                            vals += str(key)
                            break
                total += int(vals)
        return total


if __name__ == '__main__':
    s1 = time.perf_counter()
    # sol = Solution().solution('inputday8.txt')
    # print(sol)

    sol = Solution().solution_part2('inputday8.txt')
    print(sol)

    e1 = time.perf_counter()
    print(f"Time taken: {round(e1 - s1, 5)} seconds")