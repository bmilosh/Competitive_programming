"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. 
To fit it all into your refrigerator, you'll need to move it 
into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. 
If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different combinations 
of containers can exactly fit all 150 liters of eggnog?

Your puzzle answer was 1638.

--- Part Two ---

While playing with all the containers in the kitchen, 
another load of eggnog arrives! The shipping and receiving 
department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit 
all 150 liters of eggnog. How many different ways can you fill 
that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. 
There were three ways to use that many containers, and so the answer there would be 3.

Your puzzle answer was 17.
"""

from itertools import combinations


class Solution:
    def fill_containers(self, input: str, part2=False) -> int:
        with open(f"{input}", 'rt') as f:
            containers = [int(line) for line in f.readlines()]

        combs = [h for i in range(2, len(containers)) for h in combinations(containers, i) if sum(h) == 150]
        if part2:
            combs = sorted(combs, key=lambda x: len(x))
            return len([nums for nums in combs if len(nums) == len(combs[0])])
        return len(combs) 


if __name__ == '__main__':
    solution = Solution().fill_containers('input_day17.txt', part2=True)
    print(solution)
        