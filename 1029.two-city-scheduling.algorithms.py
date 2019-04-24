class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        costs.sort(key = lambda x: x[0] - x[1])
        return sum(cand[0] for cand in costs[:N]) + sum(cand[1] for cand in costs[N:])
