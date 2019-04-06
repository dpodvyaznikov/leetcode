class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        seen = {}
        for elem in A:
            if seen.get(elem, None):
                return elem
            seen[elem] = True
