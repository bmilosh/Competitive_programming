
from collections import Counter

class Solution:
    def solution1(self, input):
        with open(f"{input}") as f:
            lines = list(f.readlines())
            swap = zip(*lines)
            ns = ''
            ln = ''
            for itm in swap:
                cswap = Counter(itm)
                ns += cswap.most_common(1)[0][0]
                ln += cswap.most_common()[-1][0]
        return int(ns, 2) * int(ln, 2)


    def solution(self, input):
        with open(f"{input}") as f:
            lines = [itm.strip() for itm in f.readlines()]
            swap = list(zip(*lines))
            i = 0
            ns = lines
            while True:
                cswap = Counter(swap[i])
                if cswap['1'] >= cswap['0']:
                    ns = [val for val in ns if val[i] == '1']
                else:
                    ns = [val for val in ns if val[i] != '1']
                
                if len(ns) == 1:
                    break
                i += 1
                i = i % len(lines[0])
                swap = list(zip(*ns))
            j = 0
            print('done')
            lik = lines
            swap = list(zip(*lines))
            while True:
                cswap = Counter(swap[j])
                if cswap['0'] <= cswap['1']:
                    lik = [val for val in lik if val[j] == '0'] 
                else:
                    lik = [val for val in lik if val[j] == '1']
                if len(lik) == 1:
                    break
                j += 1
                j = j % len(lines[0])
                swap = list(zip(*lik))
            print(ns)
            print(lik)
        return int(ns[0], 2) * int(lik[0], 2)




if __name__ == '__main__':
    sol = Solution().solution('inputday3.txt')
    print(sol)