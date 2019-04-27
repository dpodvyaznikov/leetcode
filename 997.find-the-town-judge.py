class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        not_judges = {t[0] for t in trust}
        if len(not_judges) != N-1:
            return -1
        
        # My initial solution
        # person_trusted = [0] * N
        # person_trusts = [0] * N
        
        # for a, b in trust:
        #     person_trusted[b-1] += 1
        #     person_trusts[a-1] += 1
        
        # for i, num in enumerate(person_trusted):
        #     if num == N-1 and person_trusts[i] == 0:
        #         return i+1
        # return -1

        # There must be a better way
        judge = N * (N -1) // 2 - sum(not_judges)

        if [b for a,b in trust].count(judge) == N-1:
            return judge
        return -1