class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        p = 0
        res = 0
        while num:
            if num % 2 == 0:
                res += 2 ** p
            p += 1
            num //= 2
            
        return res