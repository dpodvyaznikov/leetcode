class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []

        letters = set(''.join(A))

        for letter in letters:
            counts = [word.count(letter) for word in A]
            result += [letter] * min(counts)
        return result