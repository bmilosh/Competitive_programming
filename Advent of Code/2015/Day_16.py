"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to 
send her a thank you card. However, there's a small problem: 
she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, 
you need to figure out which Aunt Sue (which you conveniently 
number 1 to 500, for sanity) gave you the gift. 
You open the present and, as luck would have it, good ol' Aunt Sue 
got you a My First Crime Scene Analysis Machine! Just what you wanted. 
Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can 
detect a few specific compounds in a given sample, as well as how 
many distinct kinds of those compounds there are. 
According to the instructions, these are what the MFCSAM can detect:

    children, by human DNA age analysis.
    cats. It doesn't differentiate individual breeds.
    Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
    goldfish. No other kinds of fish.
    trees, all in one group.
    cars, presumably by exhaust or gasoline or something.
    perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. 
You put the wrapping from the gift into the MFCSAM. 
It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. 
Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

Your puzzle answer was 373.

--- Part Two ---

As you're about to send the thank you note, 
something in the MFCSAM's instructions catches your eye. 
Apparently, it has an outdated retroencabulator, 
and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that 
there are greater than that many (due to the unpredictable 
nuclear decay of cat dander and tree pollen), while 
the pomeranians and goldfish readings indicate that 
there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

Your puzzle answer was 260.
"""


class Solution:
    def __init__(self, part2=False) -> None:
        self.real_sue = {'children': [3],
                        'samoyeds': [2],
                        'akitas': [0],
                        'vizslas': [0],
                        'cars': [2],
                        'perfumes': [1]}
        if part2:
            self.real_sue['cats'] = [i for i in range(8, 1000)]
            self.real_sue['pomeranians'] = [i for i in range(3)]
            self.real_sue['goldfish'] = [i for i in range(5)]
            self.real_sue['trees'] = [i for i in range(4, 1000)]
        else:
            self.real_sue['cats'] = [7]
            self.real_sue['pomeranians'] = [3]
            self.real_sue['goldfish'] = [5]
            self.real_sue['trees'] = [3]

    def find_real_sue(self, input: str) -> str:
        properties = {}
        with open(f"{input}", 'rt') as f:
            for line in f.readlines():
                # line will look something like the following:
                # Sue 1: cars: 9, akitas: 3, goldfish: 0
                # We add the '.' just for consistency
                line = line.strip() + '.'
                line = line.split()
                name = line[0] + line[1]
                # Sue 1: cars: 9, akitas: 3, goldfish: 0
                properties[name[:-1]] = {line[i][:-1] : int(line[i+1][:-1]) for i in range(2, len(line), 2)}

        is_real_sue = []

        for sue in properties:
            if all(properties[sue][thing] in self.real_sue[thing] for thing in properties[sue]):
                is_real_sue.append(sue)
        if is_real_sue:
            return is_real_sue[0]
        return None


if __name__ == '__main__':
    solution = Solution(part2=True).find_real_sue('aunt_sue_day16.txt')
    print(solution)