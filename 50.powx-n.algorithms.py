class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        cur = 1
        mult = x
        while n != 0:
            if n % 2:
                cur *= mult
            mult *= mult
            n = n // 2
        return cur
