"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. 
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. 
You make a list of the remaining ingredients you could use to 
finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, 
and you have to be accurate so you can reproduce your results in the future. 
The total score of a cookie can be found by adding up each of the properties 
(negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon 
(because the amounts of each ingredient must add up to 100) would result 
in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) 
results in a total score of 62842880, which happens to be the best score possible 
given these ingredients. If any properties had produced a negative total, 
it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, 
what is the total score of the highest-scoring cookie you can make?

Your puzzle answer was 18965440.

--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe 
that has exactly 500 calories per cookie (so they can use it as a meal replacement). 
Keep the rest of your award-winning process the same 
(100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of
butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie 
count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, 
the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, 
what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

Your puzzle answer was 15862900.
"""


class Solution:
    def make_cookies(self, input: str, part2=False) -> int:
        ingredients = {}
        with open(f"{input}", 'rt') as f:
            for line in f.readlines():
                # line will look something like the following:
                # Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
                # We add the '.' just for consistency
                line = line.strip() + '.'
                line = line.split()
                ingredients[line[0][:-1]] = [int(line[item][:-1]) for item in range(2, 11, 2)]

        checked_any = False
        for i in range(100):
            for j in range(100):
                if i + j > 100: 
                    break
                for k in range(100):
                    if i + j + k > 100: 
                        break
                    for m in range(100):
                        if i + j + k + m != 100: 
                            continue
                        sum1 = [i * item for item in ingredients['Frosting']]
                        sum2 = [j * item for item in ingredients['Candy']]
                        sum3 = [k * item for item in ingredients['Butterscotch']]
                        sum4 = [m * item for item in ingredients['Sugar']]
                        score = [sum(item) for item in zip(sum1, sum2, sum3, sum4) if sum(item) >= 0]

                        if len(score) < 5: 
                            # Eliminates the case where one ingredient has value 0
                            # which would make the total score for that combination 0.
                            score1 = 0 
                        else:
                            if part2 and score[4] != 500:
                                continue
                            score1 = score[0] * score[1] * score[2] * score[3]

                        if not checked_any:
                            total_score = score1
                            checked_any = True
                        else:
                            if total_score < score1:
                                total_score = score1

        return total_score  


if __name__ == '__main__':
    solution = Solution().make_cookies('cookie_ingredients_day15.txt', part2=True)
    print(f"Highest scoring cookie has a total score of {solution}.")