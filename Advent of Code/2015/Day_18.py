"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: 
now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the 
ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). 
A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration 
based on the current one. Each light's next state (either on or off) depends on 
its current state and the current states of the eight lights adjacent to it 
(including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; 
the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, 
and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

Your puzzle answer was 768.

--- Part Two ---

You flip the instructions over; Santa goes on to point out that 
this is all just an implementation of Conway's Game of Life. 
At least, it was, until you notice that something's wrong with 
the grid of lights you bought: four lights, one in each corner, 
are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, 
but with the four corners always in the on state, how many lights are on after 100 steps?

Your puzzle answer was 781.
"""


from itertools import product


class Solution:
    def fix_lights(self, input: str, total_runs: int, part2=False) -> int:
        all_lights = []
        with open(f"{input}", 'rt') as f:
            for line in f.readlines():
                # line will look something like the following (starting from the first period):
                # .##...##.##.######.#.#.##...#.#.#.#.#...#.##.#..#.#.####...#....#....###.#.#.#####....#.#.##.#.#.##.
                get_lights = []
                line = line.strip()
                for light in line:
                    if light == '#':
                        get_lights.append(1)
                    else:
                        get_lights.append(0)
                all_lights.append(get_lights)
        
        num = 0
        while num < total_runs:
            copy_lights = [[0 for i in range(100)] for j in range(100)]
            for row in range(100):
                for col in range(100):
                    if row in [0, 99] and col in [0, 99]:
                        if part2:
                            copy_lights[row][col] = 1
                            continue
                        nearby_lights = [all_lights[row - row % 2 + i][col - col % 2 + j] for i, j in product(range(2), repeat=2)]  
                    
                    elif (row in range(1, 99) and col in [0, 99]):
                        # For the lights on the left and right columns
                        nearby_lights = [all_lights[i][col - col % 2 + j] for i in range(row - 1, row + 2) for j in range(2)]

                    elif (row in [0, 99] and col in range(1, 99)):
                        # For the lights on the top and bottom rows
                        nearby_lights = [all_lights[row - row % 2 + j][i] for j in range(2) for i in range(col - 1, col + 2)]

                    else:
                        nearby_lights = [all_lights[i][j] for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)]  
                    s = sum(nearby_lights) - all_lights[row][col]
                    
                    if all_lights[row][col] == 1:  
                        if s in [2, 3]:
                            copy_lights[row][col] = 1
                    
                    else: 
                        if s == 3:
                            copy_lights[row][col] = 1
            all_lights = copy_lights
            num += 1

        return sum([sum(lights) for lights in all_lights]) 


if __name__ == '__main__':
    solution = Solution().fix_lights('lights_day18.txt', 100, part2=True)
    print(f"There are {solution} lights on in the end.")