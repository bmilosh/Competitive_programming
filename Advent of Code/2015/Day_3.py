"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

Your puzzle answer was 2081.
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

Your puzzle answer was 2341.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

class Solution:
    def get_input(self, input: str):
        with open(f"{input}", 'rt') as directions:
           return directions.read()


    def visit_houses(self, input: str) -> int:
        directions = self.get_input(input)
        visited = [[0, 0]]
        grid = [0, 0]
        total_visited = 1
        for house in directions:
            if house == '^':
                grid[0] += 1
            elif house == '>':
                grid[1] += 1
            elif house == '<':
                grid[1] -= 1
            else:
                grid[0] -= 1
            if not grid in visited:
                visited.append(grid.copy())
                total_visited += 1
    
        return total_visited


    def visit_houses_in_twos(self, input: str) -> int:
        directions = self.get_input(input)
        visited1 = [[0, 0]]
        visited2 = [[0, 0]]
        grid1 = [0, 0]
        grid2 = [0, 0]
        total_visited = 1
        for i in range(0, len(directions), 2):

            if directions[i] == '^':
                grid1[0] += 1
            elif directions[i] == '>':
                grid1[1] += 1
            elif directions[i] == '<':
                grid1[1] -= 1
            elif directions[i] == 'v':
                grid1[0] -= 1

            if not grid1 in visited1 and not grid1 in visited2:
                visited1.append(grid1.copy())
                total_visited += 1

            if i != len(directions) - 1:
                j = i + 1

                if directions[j] == '^':
                    grid2[0] += 1
                elif directions[j] == '>':
                    grid2[1] += 1
                elif directions[j] == '<':
                    grid2[1] -= 1
                elif directions[j] == 'v':
                    grid2[0] -= 1

                if not grid2 in visited2 and not grid2 in visited1:
                    visited2.append(grid2.copy())
                    total_visited += 1

        return total_visited  


if __name__ == '__main__':
    # solution1 = Solution().visit_houses('visit_houses_day3.txt')
    # print(f"{solution1} houses visited at least once.")

    solution = Solution().visit_houses_in_twos('visit_houses_day3.txt')
    print(f"{solution} houses visited at least once.")