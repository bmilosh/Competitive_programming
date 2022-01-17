

class Solution:
    def solution(self, input):
        hor = 0
        dep = 0
        with open(f"{input}") as f:
            for line in f:
                line = line.strip().split()
                if line[0].startswith('f'):
                    hor += int(line[1])
                if line[0].startswith('d'):
                    dep += int(line[1])
                if line[0].startswith('u'):
                    dep -= int(line[1])
        return hor * dep


    def solution2(self, input):
        with open(f"{input}") as f:
            lines = list(f.readlines())
            hor = sum(int(line.strip().split()[1]) for line in lines if line.startswith('f'))
            dep = sum(int(line.strip().split()[1]) if line.startswith('d') else -int(line.strip().split()[1]) for line in lines)
        return hor * (dep + hor)


    def solution_part2(self, input):
        hor = 0
        aim = 0
        dep = 0
        with open(f"{input}") as f:
            for line in f:
                line = line.strip().split()
                if line[0].startswith('f'):
                    hor += int(line[1])
                    dep += aim * int(line[1])
                if line[0].startswith('d'):
                    aim += int(line[1])
                if line[0].startswith('u'):
                    aim -= int(line[1])
        return hor * dep


if __name__ == '__main__':
    sol = Solution().solution2('inputday2.txt')
    print(sol)