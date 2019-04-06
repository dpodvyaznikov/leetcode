class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        s_xy = sum(h > 0 for row in grid for h in row)
        s_xz = sum(map(max, grid))
        s_yz = sum(map(max, zip(*grid)))

        return s_xy + s_xz + s_yz
