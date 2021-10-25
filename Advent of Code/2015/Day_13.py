"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. 
Not everyone gets along! This year, you resolve, will be different. 
You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their 
happiness would increase or decrease if they were to find themselves sitting 
next to each other person. You have a circular table that will be just 
big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, 
and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units 
(because David talks so much), but David would gain 46 happiness units 
(because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice 
(Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob 
(Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). 
The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, 
you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?

Your puzzle answer was 733.

--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself. 
At this point, you're pretty apathetic toward the whole thing, 
and your happiness wouldn't really go up or down regardless of 
who you sit next to. You assume everyone else would be just as 
ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

Your puzzle answer was 725.
"""
from itertools import permutations
from typing import Tuple


class Solution:
    def find_optimal_seating(self, input: str, part2=False) -> Tuple[int, str]:
        connections = []
        people = []
        with open(f"{input}", 'rt') as f:
            for line in f.readlines():
                # line will look something like the following:
                # Alice would gain 2 happiness units by sitting next to Bob.
                line1 = line.split()
                people.append(line1[0])
                connections.append([line1[0], line1[-1][:-1]])
                if line1[2] == 'gain':
                    connections.append(int(line1[3]))
                else:
                    connections.append(-1 * int(line1[3]))

        people = list(set(people))
        if part2:
            for person in people:
                connections.extend([['Me', person], 0])
                connections.extend([[person, 'Me'], 0])
            people.append('Me')
        perms = [perm for perm in permutations(range(len(people)))]
        # List of all possible arrangements.

        i = 0
        while i < len(perms):
            perm = perms[i]
            happiness_for_perm = 0
            j = 0

            while j < len(perm):
                right_pair = [people[perm[j]], people[perm[(j + 1) % len(perm)]]]
                left_pair = [people[perm[j]], people[perm[(j - 1) % len(perm)]]]
                happiness_for_perm += (connections[connections.index(right_pair) + 1] +
                                    connections[connections.index(left_pair) + 1])
                j += 1

            if i == 0:
                optimal_happiness_value = happiness_for_perm
                optimal_perm = perm
            else:
                if optimal_happiness_value < happiness_for_perm:
                    optimal_happiness_value = happiness_for_perm
                    optimal_perm = perm
            i += 1

        return optimal_happiness_value, self.show_arrangement([people[k] for k in optimal_perm])


    def show_arrangement(self, arrangement: list) -> str:
        arrangement_str = '' 
        for i in range(len(arrangement) - 1):
            arrangement_str += arrangement[i] + ' -> '
        return arrangement_str + arrangement[-1]


if __name__ == '__main__':
    solution1 = Solution().find_optimal_seating('round_table_day13.txt', part2=True)
    print(*solution1, sep='\n')