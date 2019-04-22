class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
# My initial solution:
#         p = 0
#         for row in grid:
#             p = self.count_in_row(row, p)
#         for row in list(zip(*grid)):
#             p = self.count_in_row(row, p)
#         return p

#     @staticmethod
#     def count_in_row(row, p=0):
#         count = 0
#         prev_elem = 0
#         for i, elem in enumerate(row):
#             count += 1
#             if elem == 1 and prev_elem == 0:
#                 p += 1
#             elif elem == 0 and prev_elem == 1:
#                 p += 1
#             if count == len(row) and elem == 1:
#                 p += 1
#             prev_elem = elem
#         return p

# More pythonic way of doing pretty the same thing 
# that I saw in StefanPochmann's post
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
           for row in grid + list(map(list, zip(*grid))))