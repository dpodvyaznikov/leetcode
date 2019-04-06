class Solution:
    def peakIndexInMountainArray(self, A):
        low, high = 0, len(A) - 1
        while high > low:
            mid = low + (high - low) // 2
            if A[mid+1] > A[mid]:
                low = mid + 1
            else:
                high = mid
        return low