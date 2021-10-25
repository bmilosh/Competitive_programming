
"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday 
house decorating contest year after year, you've decided 
to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, 
Santa has mailed you instructions on how to display the 
ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; 
the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. 
The instructions include whether to turn on, turn off, or toggle 
various inclusive ranges given as coordinate pairs. Each coordinate 
pair represents opposite corners of a rectangle, inclusive; 
a coordinate pair like 0,0 through 2,2 therefore refers to 9 
lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set 
up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, 
        turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

Your puzzle answer was 377891.

--- Part Two ---

You just finish implementing your winning light pattern when 
you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; 
each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase 
the brightness of those lights by 1.

The phrase turn off actually means that you should decrease 
the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase 
the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

Your puzzle answer was 14110788.
"""

import re


class Solution:
    def lights_setup(self, file: str, part2=False) -> int:
        initial_setup = [[0 for num1 in range(1000)] for num2 in range(1000)] 

        with open(f'{file}', 'rt') as f:
            for line in f:
                # line will look something like the following:
                # turn on 887,9 through 959,629
                grid = re.findall(r"[0-9,0-9]+", line)
                extract_grid = [int(item1) for item in grid for item1 in item.split(',')]
                to_check = [(i,j) for i in range(extract_grid[0], extract_grid[2] + 1) 
                            for j in range(extract_grid[1], extract_grid[3] + 1)]
                
                if line.startswith('turn on'):
                    for row, col in to_check:
                        if not part2:
                            initial_setup[row][col] = 1
                        else:
                            initial_setup[row][col] += 1
                
                elif line.startswith('turn off'):
                    for row, col in to_check:
                        if not part2:
                            initial_setup[row][col] = 0
                        else:
                            initial_setup[row][col] = max(initial_setup[row][col] - 1, 0)
                
                else:
                    # for example: toggle 294,259 through 474,326
                    for row, col in to_check:
                        if not part2:
                            initial_setup[row][col] = (initial_setup[row][col] + 1) % 2
                        else:
                            initial_setup[row][col] += 2 

        return sum([sum(sublist) for sublist in initial_setup]) 


if __name__ == '__main__':
    solution = Solution().lights_setup('fire_hazard_day6.txt')
    print(f"{solution} have their lights turned on in the end.", part2=True)
