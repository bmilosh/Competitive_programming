import re
import time


class Solution:
    def __init__(self, input) -> None:
        self.min_r, self.max_r = float("inf"), 0
        self.min_c, self.max_c = float("inf"), 0
        self.comnds = []
        patrn = re.compile("(\d+),(\d+) -> (\d+),(\d+)")
        with open(f"{input}") as f:
            lines = list(f.readlines())
            for line in lines:
                mat = patrn.match(line.strip())
                self.min_r = min(self.min_r, min(
                    int(mat.group(2)), int(mat.group(4))))
                self.max_r = max(self.max_r, max(
                    int(mat.group(2)), int(mat.group(4))))
                self.min_c = min(self.min_c, min(
                    int(mat.group(1)), int(mat.group(3))))
                self.max_c = max(self.max_c, max(
                    int(mat.group(1)), int(mat.group(3))))
                self.comnds.append([int(mat.group(2)), int(
                    mat.group(1)), int(mat.group(4)), int(mat.group(3))])
        self.grid = [[0 for _ in range(self.min_c, self.max_c + 1)]
                     for _ in range(self.min_r, self.max_r + 1)]

    def solution(self):
        for comnd in self.comnds:
            if comnd[0] != comnd[2] and comnd[1] != comnd[3]:
                continue
            for i in range(min(comnd[0], comnd[2]) - self.min_r, max(comnd[0], comnd[2]) + 1 - self.min_r):
                for j in range(min(comnd[1], comnd[3]) - self.min_c, max(comnd[1], comnd[3]) + 1 - self.min_c):
                    self.grid[i][j] += 1

        return sum(sum(1 for itm in row if itm > 1) for row in self.grid)

    def solution_part2(self):

        for comnd in self.comnds:
            if comnd[0] != comnd[2] and comnd[1] != comnd[3]:
                if abs(comnd[0] - comnd[2]) == abs(comnd[1] - comnd[3]):

                    if not (left := list(range(comnd[0] - self.min_r, comnd[2] - self.min_r + 1))):
                        left = list(
                            range(comnd[0] - self.min_r, comnd[2] - self.min_r - 1, -1))
                    if not (right := list(range(comnd[1] - self.min_c, comnd[3] - self.min_c - 1, -1))):
                        right = list(
                            range(comnd[1] - self.min_c, comnd[3] - self.min_c + 1))
                    diags = list(zip(left, right))

                    for pair in diags:
                        self.grid[pair[0]][pair[1]] += 1
                continue
            for i in range(min(comnd[0], comnd[2]) - self.min_r, max(comnd[0], comnd[2]) + 1 - self.min_r):
                for j in range(min(comnd[1], comnd[3]) - self.min_c, max(comnd[1], comnd[3]) + 1 - self.min_c):
                    self.grid[i][j] += 1

        return sum(sum(1 for itm in row if itm > 1) for row in self.grid)


if __name__ == '__main__':
    s1 = time.perf_counter()
    # sol = Solution('inputday5.txt').solution()
    # print(sol)

    sol = Solution('inputday5.txt').solution_part2()
    print(sol)

    e1 = time.perf_counter()
    print(e1 - s1)
