class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        whole_sum = sum(A)
        
        if whole_sum % 3 != 0:
            return False
        
        equal_sum = whole_sum // 3
        
        cumsum = 0
        
        for elem in A:
            cumsum += elem
            if cumsum == equal_sum:
                cumsum = 0
        return not cumsum