import time


class Solution:
    def solution(self, input, part2=False):
        with open(f"{input}") as f:
            lines = list(map(int, f.read().strip().split(',')))
            m = float("inf")
            def lam_fun(x): return (x * (x + 1)) / 2
            for pos, val in enumerate(lines):
                if not part2:
                    s = sum(abs(val - lines[i])
                            for i in range(len(lines)) if i != pos)
                else:
                    s = sum(map(lam_fun, [abs(pos - lines[i])
                            for i in range(len(lines))]))
                m = min(m, s)
        return m


if __name__ == '__main__':
    s1 = time.perf_counter()
    sol = Solution().solution('inputday7.txt', True)
    print(sol)

    e1 = time.perf_counter()
    print(f"Time taken: {round(e1 - s1, 3)} seconds")
