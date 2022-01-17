import time
from itertools import product


class Solution:
    def __init__(self, input) -> None:
        with open(f"{input}") as f:
            lines = list(f.readlines())
            self.locs1 = [list(map(int, list(line.strip()))) for line in lines]
            self.visited = [[0] * len(self.locs1)
                            for _ in range(len(self.locs1))]

    def graph_logic(self, current_total, decider=1, part2=False):
        stack = []
        for i in range(len(self.locs1)):
            for j in range(len(self.locs1[0])):
                self.locs1[i][j] = (self.locs1[i][j] + decider) % 10
                if self.locs1[i][j] == 0:
                    stack.append((i, j))

        while stack:
            r, c = stack.pop()
            if self.visited[r][c]:
                continue
            self.visited[r][c] = 1
            if not part2:
                current_total += 1
            neigbs = self.find_neigbs(r, c)
            for new_r, new_c in neigbs:
                if self.visited[new_r][new_c]:
                    continue
                elif self.locs1[new_r][new_c] == 0:
                    if (new_r, new_c) not in stack:
                        stack.append((new_r, new_c))
                else:
                    self.locs1[new_r][new_c] = (
                        self.locs1[new_r][new_c] + 1) % 10
                    if self.locs1[new_r][new_c] == 0:
                        stack.append((new_r, new_c))
        self.visited = [[0] * len(self.locs1)
                        for _ in range(len(self.locs1))]
        return current_total

    def solution(self, runs):
        decider = 10 - max(max(row) for row in self.locs1)
        runs -= min(runs, decider)
        current_total = 0
        counter = 0
        while runs > 0:
            current_total = self.graph_logic(current_total, decider)
            decider = 10 - max(max(row) for row in self.locs1)
            counter += len([1 for row in self.locs1 for itm in row if itm == 0])

            runs -= min(runs, decider)
            if runs < decider:
                break

        return current_total

    def solution_part2(self):
        current_total = 0
        while True:
            self.graph_logic(current_total)
            current_total += 1
            self.visited = [[0] * len(self.locs1)
                            for _ in range(len(self.locs1))]
            if all(itm == 0 for row in self.locs1 for itm in row):
                break

        return current_total

    def find_neigbs(self, i, j):
        neigbs = [(i + k, j + m)
                  for k, m in product([-1, 0, 1], repeat=2)
                  if 0 <= i + k < len(self.locs1) and 0 <= j + m < len(self.locs1) and (k, m) != (0, 0)]
        return neigbs


if __name__ == '__main__':
    s1 = time.perf_counter()
    sol = Solution('inputday11.txt').solution(101)
    print(sol)

    sol = Solution('inputday11.txt').solution_part2()
    print(sol)

    e1 = time.perf_counter()
    print(f"Time taken: {round(e1 - s1, 5)} seconds")
