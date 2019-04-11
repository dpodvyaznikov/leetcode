class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines, length = 1, 0

        for letter in S:
            width = widths[ord(letter) - 97]
            length += width
            if length > 100:
                length = width
                lines += 1

        return [lines, length]