class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        res = [[val^1 for val in l][::-1] for l in A]
        return res
