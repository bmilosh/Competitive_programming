import re


class Solution:
    def solution(self, input, numrows, numcols, part2=False):
        patrn = re.compile(".+ ([x,y])=(\d+)")
        grid = [['.'] * numcols for _ in range(numrows)]
        with open(f"{input}") as f:
            lines = [line.strip() for line in f.readlines()]
            for line in lines:
                if not line:
                    continue
                if line.__contains__(','):
                    c, r = map(int, line.split(','))
                    grid[r][c] = '#'
                else:
                    nonzeroes = 0
                    mat = patrn.match(line.strip())
                    if mat.group(1) == 'x':
                        along = int(mat.group(2))
                        newgrid = [['.'] * along for _ in range(len(grid))]
                        for i in range(len(grid)):
                            for j in range(along):
                                if grid[i][j] == '#' or grid[i][len(grid[0]) - 1 - j] == '#':
                                    newgrid[i][j] = '#'
                                    nonzeroes += 1
                    else:
                        along = int(mat.group(2))
                        newgrid = [['.'] * len(grid[0]) for _ in range(along)]
                        for i in range(along):
                            for j in range(len(grid[0])):
                                if grid[i][j] == '#' or grid[len(grid) - 1 - i][j] == '#':
                                    newgrid[i][j] = '#'
                                    nonzeroes += 1

                    grid = newgrid
                    if not part2:
                        break
        if part2:
            # Print the computation to a .txt file so as to be
            # able to see the final position of the grid.
            print(*grid, sep='\n')
        return nonzeroes



if __name__ == '__main__':
    sol = Solution().solution('inputday13.txt', 895, 1311, True)
    print(sol)

    # The answer for part 2 is in day13_solution.txt