import time


class Solution:
    def __init__(self) -> None:
        self.dict1 = {')' : 3,
                      ']' : 57,
                      '}' : 1197,
                      '>' : 25137}

        self.dict11 = {'(' : 1,
                      '[' : 2,
                      '{' : 3,
                      '<' : 4}

        self.pairs = {')' : '(', 
                        ']' : '[', 
                        '}' : '{', 
                        '>': '<'}

    def solution(self, input, part1=True):
        if part1:
            self.dict2 = {k: 0 for k in self.dict1}
        else:
            vals = []
        with open(f"{input}") as f:
            lines = list(f.readlines()) 
            for line in lines:
                line = line.strip()
                stack = []
                for itm in line:
                    if not itm in self.pairs:
                        stack.append(itm)
                    else:
                        if stack[-1] == self.pairs[itm]:
                            stack.pop()
                        else:
                            if part1:
                                self.dict2[itm] += 1
                            else:
                                stack.clear()
                            break
                if not part1:
                    total = 0
                    while stack:
                        brak = stack.pop()
                        total = 5 * total + self.dict11[brak]
                    if total:
                        vals.append(total)

        if part1:
            return sum(val * self.dict1[key] for key, val in self.dict2.items())
        return sorted(vals)[len(vals) // 2]



if __name__ == '__main__':
    s1 = time.perf_counter()
    sol = Solution().solution('inputday10.txt', False)
    print(sol)

    e1 = time.perf_counter()
    print(f"Time taken: {round(e1 - s1, 3)} seconds")