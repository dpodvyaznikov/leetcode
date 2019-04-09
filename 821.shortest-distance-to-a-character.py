class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_inds = [None,]
        for i, char in enumerate(S):
            if char == C:
                c_inds.append(i)
        c_inds.append(None)

        res = [None] * len(S)

        for i in range(len(c_inds)-1):
            ind_start = c_inds[i]
            ind_end = c_inds[i+1]
            if ind_start is None:
                for j in range(0, ind_end):
                    res[j] = ind_end - j
            elif ind_end is None:
                for j in range(ind_start, len(S)):
                    res[j] = j - ind_start
            else:
                ind_mid = ind_start + (ind_end - ind_start) // 2
                for j in range(ind_start, ind_mid + 1):
                    res[j] = j - ind_start
                for j in range(ind_mid + 1, ind_end):
                    res[j] = ind_end - j

        return res
