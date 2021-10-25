"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; 
his elves have provided him the distances between every 
pair of locations. He can start and end at any two 
(different) locations he wants, but he must visit each 
location exactly once. What is the shortest distance 
he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, 
and so the answer is 605 in this example.

What is the distance of the shortest route?

Your puzzle answer was 251.

--- Part Two ---

The next year, just to show off, Santa decides to take 
the route with the longest distance instead.

He can still start and end at any two (different) locations 
he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route 
would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

Your puzzle answer was 898.
"""

from itertools import permutations
from typing import Tuple


class Solution:
    def show_path(self, path: list) -> str:
        path_str = '' 
        for i in range(len(path) - 1):
            path_str += path[i] + ' -> '
        return path_str + path[-1]


    def find_shortest_path(self, input: str, part2=False) -> Tuple[list, int]:
        
        # We extract all connections into a list of lists. 
        # The first entry in each connection is a pair of locations, contained in a set.
        # The second entry is the distance between the pair of locations in the first entry.

        # We also store all locations in a separate list. We'll work with that to generate possible routes.
        with open(f"{input}", 'rt') as f:
            connections = [[{item[0], item[2]}, int(item[4])] for item in [line.strip().split() for line in f.readlines()]]
        cities = list({item for triple in connections for item in triple[0]} )

        pos_perms = [i for i in permutations(range(len(cities)), len(cities))]

        for i in range(len(pos_perms)):
            poss_solution = pos_perms[i]
            distance = 0
            found1 = 1  # Used to indicate that the permutation is valid (i.e, there's a path from the first item to the last).

            for j in range(len(poss_solution) - 1):
                duo = [poss_solution[j], poss_solution[j + 1]]
                duo1 = {cities[duo[0]], cities[duo[1]]}
                found = 0  # Used to indicate that there is an edge between adjacent nodes.

                for triple in connections:
                    if triple[0] == duo1:
                        distance += triple[1]
                        found = 1
                        break
                if found == 0:
                    found1 = 0 # We found a pair of adjacent nodes with no edge. Hence, this permutation is not valid.
                    break

            if found1 == 1:
                if i == 0:
                    # We initialize the minimum distance and path
                    min_dist = distance
                    max_distance = distance
                    min_path = poss_solution
                    max_path = poss_solution
                else:
                    if min_dist > distance:
                        min_dist = distance
                        min_path = poss_solution
                    if max_distance < distance:
                        max_distance = distance
                        max_path = poss_solution
        if part2:
            return self.show_path([cities[i] for i in max_path]), max_distance
        return self.show_path([cities[i] for i in min_path]), min_dist


if __name__ == '__main__':
    solution = Solution().find_shortest_path('shortest_distance_day9.txt', part2=True)
    print(f"The longest path is {solution[0]} with distance {solution[1]}")
    # print(f"The shortest path is {solution[0]} with distance {solution[1]}")    