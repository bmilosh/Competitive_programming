
class Solution:
    def solution(self, input):
        with open(f"{input}") as f:
            lines = list(f.readlines())
            call_order = lines[0].strip().split(',')
            boards = {i: [line.strip().split() for line in lines[i + 1: i + 6]]
                      for i in range(1, len(lines), 6)}
            last = -1
            cur = 0
            for board in boards:
                for i in range(5):
                    row = boards[board][i]
                    inds = [call_order.index(card) for card in row]
                    if (m := max(inds)) < last or last == -1:
                        last = m
                        cur = board
                for col in range(5):
                    inds = [call_order.index(card) for card in [
                        boards[board][i][col] for i in range(5)]]
                    if (m := max(inds)) < last:
                        last = m
                        cur = board
            sums = 0
            for board in boards[cur]:
                sums += sum(int(itm)
                            for itm in board if call_order.index(itm) > last)

        return sums * int(call_order[last])

    def solution_part2(self, input):
        with open(f"{input}") as f:
            lines = list(f.readlines())
            call_order = lines[0].strip().split(',')
            boards = {i: [line.strip().split() for line in lines[i + 1: i + 6]]
                      for i in range(1, len(lines), 6)}
            fill_order = {}
            for board in boards:
                inds = min([max(call_order.index(card)
                           for card in boards[board][i]) for i in range(5)])
                inds2 = min([max(call_order.index(card)
                                 for card in [boards[board][j][col]
                                              for j in range(5)])
                            for col in range(5)])
                fill_order[board] = min(inds, inds2)
            winner = [key for key in fill_order if fill_order[key]
                      == max(fill_order.values())]
            win_val = max(fill_order.values())
            sums = sum(sum(int(itm) if call_order.index(itm) > win_val else 0 for itm in board)
                       for board in boards[winner[0]])
        return sums * int(call_order[win_val])


if __name__ == '__main__':
    sol = Solution().solution_part2('inputday4.txt')
    print(sol)
