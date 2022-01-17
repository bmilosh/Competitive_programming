import heapq
import time
from itertools import product


class Solution:
    def solution(self, input):
        with open(f"{input}") as f:
            self.lines = [list(map(int, list(line.strip())))
                          for line in f.readlines()]
            return self.graph_logic()

    def graph_logic(self):
        lines_length = len(self.lines)
        self.distance = [[float('inf')] * len(self.lines[0])
                         for _ in range(lines_length)]
        self.visited = [[0] * len(self.lines[0]) for _ in range(lines_length)]
        self.distance[0][0] = 0
        queue = [(0, (0, 0))]
        heapq.heapify(queue)
        while queue:
            dist, node = heapq.heappop(queue)
            if self.visited[node[0]][node[1]]:
                continue
            if (node[0], node[1]) == (len(self.lines) - 1, len(self.lines[0]) - 1):
                return self.distance[-1][-1]
            self.visited[node[0]][node[1]] = 1
            if node == (0, 0):
                neigbs = self.find_neigbs(0, 0)
            else:
                neigbs = self.find_neigbs(*node)
            for nodes in neigbs:
                my_dist = dist + self.lines[nodes[0]][nodes[1]]
                if not self.visited[nodes[0]][nodes[1]] and my_dist < self.distance[nodes[0]][nodes[1]]:
                    nodes += ((node[0], node[1]),)
                    heapq.heappush(queue, (my_dist, nodes))
                    self.distance[nodes[0]][nodes[1]] = my_dist

    def solution_part2(self, input):
        with open(f"{input}") as f:
            self.lines1 = [list(map(int, list(line.strip())))
                           for line in f.readlines()]
            self.lines = [[0 for _ in range(len(self.lines1[0] * 5))]
                          for _ in range(len(self.lines1 * 5))]

            for i in range(len(self.lines1)):
                for j in range(len(self.lines1[0])):
                    for k, m in product(range(5), repeat=2):
                        if self.lines1[i][j] + k + m != 9:
                            ans = (self.lines1[i][j] + k + m) % 9
                        else:
                            ans = 9
                        self.lines[i + (len(self.lines1) * k)
                                   ][j + (len(self.lines1) * m)] = ans

            return self.graph_logic()

    def find_neigbs(self, i, j, parent=None):
        neigbs = [(m + i, n + j)
                  for m, n in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                  if 0 <= m + i < len(self.lines) and
                  0 <= n + j < len(self.lines[0])]
        if parent:
            neigbs.remove(parent)

        return neigbs


if __name__ == '__main__':
    s1 = time.perf_counter()
    # sol = Solution().solution('inputday15.txt')
    # print(sol)

    sol = Solution().solution_part2('inputday15.txt')
    print(sol)
    e1 = time.perf_counter()
    print(round(e1 - s1, 3))
