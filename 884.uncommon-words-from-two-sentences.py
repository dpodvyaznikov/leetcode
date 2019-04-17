class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words = {}
        for word in ' '.join([A, B]).split(" "):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        return [key for key, val in words.items() if val==1]
