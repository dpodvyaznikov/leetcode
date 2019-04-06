class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:

        diff = max(A) - min(A)

        if diff < 2*K:
            return 0
        else:
            return diff - 2*K
