"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH

Given the replacements above and starting with HOH, the following molecules could be generated:

    HOOH (via H => HO on the first H).
    HOHO (via H => HO on the second H).
    OHOH (via H => OH on the first H).
    HOOH (via H => OH on the second H).
    HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

--- Part Two ---

Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH

If you'd like to make HOH, you start with e, and then make the following replacements:

    e => O to get O
    O => HH to get HH
    H => OH (on the second H) to get HOH

So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

"""


def distinct_molecules(input):
    replacements = {}
    with open(f"{input}", 'rt') as f:
        alllines = f.readlines()
        for line in alllines[:-2]:
            if line == []:
                continue
            line = line.strip().split()
            if line[0] not in replacements:
                replacements[line[0]] = [line[2]]
            else:
                replacements[line[0]].append(line[2])
        molecule = alllines[-1]

    mole_hash = []
    for mole in replacements:
        appears = molecule.count(mole)
        start_from = 0
        for i in range(appears):
            mole_ind = molecule.find(mole, start_from)
            if mole_ind == -1: continue
            for replacement in replacements[mole]:
                temp_molecule = molecule[:mole_ind] + replacement + molecule[len(mole) + mole_ind:]
                mhash = hash(temp_molecule)
                if mhash not in mole_hash:
                    mole_hash.append(mhash)
            start_from = len(mole) + mole_ind
    # print(*mole_hash[:3], sep='\n')
    print()
    print(len(mole_hash))


def recursive_distinct_molecules(molecules: str, replacements: dict, starter='', steps=0):
    if len(starter) == len(molecules):
        return 1
    elif len(starter) > len(molecules):
        return -1

    if not steps:
        options = replacements['e']
        # O8 = {}
        # O8.update()

def distinct_molecules_part2(input):
    replacements = {}
    with open(f"{input}", 'rt') as f:
        alllines = f.readlines()
        for line in alllines[:-2]:
            if line == []:
                continue
            line = line.strip().split()
            if line[0] not in replacements:
                replacements[line[0]] = [line[2]]
            else:
                replacements[line[0]].append(line[2])
        molecule = alllines[-1]

    options = replacements['e']
    fewest_steps = 0
    steps = 0
    for starter in options:
        begin = starter
        steps += 1
        for mole in replacements:
            if mole == 'e' or not begin.__contains__(mole):
                continue
            if len(begin) > len(molecule):
                break
            if begin == molecule:
                fewest_steps = min(fewest_steps, steps)

    # for mole in replacements:
    #     appears = molecule.count(mole)
    #     start_from = 0
    #     for i in range(appears):
    #         mole_ind = molecule.find(mole, start_from)
    #         if mole_ind == -1: continue
    #         for replacement in replacements[mole]:
    #             temp_molecule = molecule[:mole_ind] + replacement + molecule[len(mole) + mole_ind:]
    #             mhash = hash(temp_molecule)
    #             if mhash not in mole_hash:
    #                 mole_hash.append(mhash)
    #         start_from = len(mole) + mole_ind
    # # print(*mole_hash[:3], sep='\n')
    # print()
    # print(len(mole_hash))


# if __name__ == '__main__':
#     distinct_molecules('medicine_day19.txt')

    # distinct_molecules('tri1.txt')

def count_prefix(input: list[str]):
    smallest_item = min(input, key=len)
    # print(smallest_item)

    counter = 0
    while counter < len(smallest_item):
        # print(smallest_item[:counter + 1])
        if all(itm.startswith(smallest_item[:counter + 1]) for itm in input):
            counter += 1
            # print(f"counter from while loop {counter}")
        else:
            # counter -= 1
            break
    return counter

# print(count_prefix(['max','maxy','manymen','mex']))
# d = ''

def remove_char(input: str, k: int):
    # for i in range(1, len(input)):
    #     if i >= len(input):
    #         break
    #     if input[i:].count(input[i - 1]) >= k - 1:
    #         input = input[:i].replace(input[i - 1], '') + input[i:].replace(input[i - 1], '')
    # for i in range(len(input)):
    #     print(i, input)
    #     if i >= len(input):
    #         break
    #     if input[i:].count(input[i - 1]) >= k - 1:
    #         print(input[i - 1])
    #         if i > 0:
    #             input = input[:i - 1] + input[i:].replace(input[i - 1], '')
    #         else:
    #             input = input.replace(input[i - 1], '')
    #             i = 0
    #     print(i, input)
    # i = 0
    # while True:
    #     checker = 0
    #     if i >= len(input):
    #         break
    #     if input[i:].count(input[i - 1]) >= k :
    #         if i > 0:
    #             input = input[:i - 1] + input[i:].replace(input[i - 1], '')
    #             i -= 1
    #         else:
    #             input = input.replace(input[i - 1], '')
    #             i = 0
    #         checker = 1
    #     else:
    #         i += 1
    #     print(i, input)

    i = 0
    while True:
        checker = 0
        if len(input) - i < k:
            break
        if i >= len(input):
            break
        if input.count(input[i]) >= k :
            input = input.replace(input[i], '')
            if i > 0:
                i -= 1
            else:
                i = 0
        else:
            i += 1
        print(i, input)        
        # if checker == 0:
        #     break
    return input

print(remove_char('geeksmmforgeeks', 2))