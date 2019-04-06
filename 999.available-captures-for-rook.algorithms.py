class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        other_rep = list()
        print(len(other_rep))
        for i in range(8):
            other_rep.append(list())
            for j in range(8):
                other_rep[i].append(board[j][i])

        def count(board, n = 0):
            b = [''.join(l).replace('.', '') for l in board]
            for l in b:
                if 'Rp' in l:
                    n += 1
                if 'pR' in l:
                    n += 1
            return n

        return count(board) + count(other_rep)
