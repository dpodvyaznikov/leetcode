class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left + 1 < right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            res = left
        else:
            res = -1
        return res
