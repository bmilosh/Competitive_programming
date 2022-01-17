import re
import math
import time
from collections import Counter


class Solution:

    def solution(self, input, days):
        """
        Since we know that the elements of the sequence will always
        be in the range(0, 9) we don't have to keep the whole sequence.
        Instead, we keep track of changes to the length of the sequence
        and its composition as days pass by using a Counter.
        Hence, we do O(8) work in each iteration of the while loop
        and O(days) iterations.
        """
        with open(f"{input}") as f:
            lines = [int(itm) for itm in f.read().strip().split(',')]
        count_lines = Counter(lines)

        while days > 0:
            sm = min(count_lines) + 1
            if days < sm:
                return sum(count_lines.values())
            temp = [(key - sm, count_lines[key])
                    for key in count_lines if key != sm - 1]
            spec = count_lines[sm - 1]
            count_lines.clear()
            count_lines = dict(temp)
            try:
                count_lines[6] += spec
            except KeyError:
                count_lines[6] = spec
            count_lines[8] = spec
            days -= min(sm, days)
        return sum(count_lines.values())


if __name__ == '__main__':
    s1 = time.perf_counter()
    sol = Solution().solution('inputday6.txt', 80)
    print(sol)
    e1 = time.perf_counter()
    print(f"Time taken: {round(e1 - s1, 3)} seconds.")
