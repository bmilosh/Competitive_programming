import math
import time
import heapq


class Solution:
    def solution(self, input):
        with open(f"{input}") as f:
            nums = 0
            lines = list(f.readlines())
            locs1 = [list(map(int, list(line.strip()))) for line in lines]
            for i in range(len(locs1)):
                row = locs1[i]
                for j in range(len(locs1[0])):
                    neigbs = [locs1[i + k][j + m]
                              for k, m in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                              if 0 <= i + k < len(locs1) and 0 <= j + m < len(locs1[0])]
                    if row[j] < min(neigbs):
                        nums += row[j] + 1
        return nums

    def find_neigbs(self, i, j):
        neigbs = []
        for k, m in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (0 <= i + k < len(self.locs) and 0 <= j + m < len(self.locs[0]) and
                    not self.visited[i + k][j + m]):  
                neigbs.append((self.locs[i + k][j + m], i + k, j + m))
        return neigbs

    def solution_part2(self, input):
        with open(f"{input}") as f:
            lines = list(f.readlines())
            locs1 = [list(map(int, list(line.strip()))) for line in lines]
            self.locs = locs1
            self.visited = [
                [9 if row[i] == 9 else 0 for i in range(len(row))] for row in locs1]

            maxlocs = []
            j = 0
            while j < len(locs1):
                row = locs1[j]
                if sum(self.visited[j]) == len(row):
                    j += 1
                    continue

                stack = []
                k = 0
                while k < len(row):
                    run_tot = 0
                    if self.visited[j][k]:
                        k += 1
                        continue
                    stack.append((row[k], j, k))
                    while stack:
                        loc = stack.pop()
                        if not self.visited[loc[1]][loc[2]]:
                            self.visited[loc[1]][loc[2]] = 1
                            run_tot += 1
                        neigbs = self.find_neigbs(loc[1], loc[2])
                        stack.extend(neigbs)
                    k += 1
                    maxlocs.append(run_tot)
                j += 1
        max3products = math.prod(heapq.nlargest(3, maxlocs))
        return max3products


if __name__ == '__main__':
    s1 = time.perf_counter()
    # sol = Solution().solution('inputday9.txt')
    # print(sol)

    sol = Solution().solution_part2('inputday9.txt')
    print(sol)

    e1 = time.perf_counter()
    print(f"Time taken: {round(e1 - s1, 5)} seconds")
