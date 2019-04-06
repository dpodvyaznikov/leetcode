class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1
        for _ in range(2, n+1):
            next_val = prev + cur
            prev = cur
            cur = next_val
        return cur
