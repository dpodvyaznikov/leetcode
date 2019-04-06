class Solution:
    def trap(self, height: List[int]) -> int:
        """
        """
        max_element_index = 0
        for i in range(len(height)):
            if height[i] > height[max_element_index]:
                max_element_index = i

        result = 0

        left_max = 0
        for i in range(max_element_index):
            left_max = max(left_max, height[i])
            result += left_max - height[i]

        right_max = 0
        for i in range(len(height)-1, max_element_index, -1):
            right_max = max(right_max, height[i])
            result += right_max - height[i] 

        return result
