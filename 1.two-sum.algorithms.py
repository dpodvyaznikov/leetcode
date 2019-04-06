class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffs = {}
        for idx, num in enumerate(nums):
            if num in diffs:
                return diffs[num], idx
            diffs[target-num] = idx
        return -1
