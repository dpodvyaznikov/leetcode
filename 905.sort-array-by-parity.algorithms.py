class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        pointer = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[pointer], A[i] = A[i], A[pointer]
                pointer += 1
        return A
