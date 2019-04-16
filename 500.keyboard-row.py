class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = 'qwertyuiopQWERTYUIOP'
        r2 = 'asdfghjklASDFGHJKL'
        r3 = 'zxcvbnmZXCVBNM'

        res = []

        for word in words:
            one_row = False
            for row in r1,r2,r3:
                if all([letter in row for letter in word]):
                    res.append(word)
        return res
