class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        first_pos_ix = 0
        for val in A:
            if val < 0:
                first_pos_ix += 1
            else:
                break

        sort_sq = []
        i = first_pos_ix -1
        j = first_pos_ix
        
        while i >= 0 and j <= N-1:
            if A[i]**2 <= A[j]**2:
                sort_sq.append(A[i]**2)
                i -= 1
            else:
                sort_sq.append(A[j]**2)
                j += 1
        if i < 0:
            while j <= len(A) - 1:
                sort_sq.append(A[j]**2)
                j += 1
        if j >= len(A):
            while i >= 0:
                sort_sq.append(A[i]**2)
                i -= 1
        return sort_sq
