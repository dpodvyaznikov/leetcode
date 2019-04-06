class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        s = sum(val for val in A if val % 2 == 0)

        for i, elem in enumerate(queries):
            val, index = elem

            if A[index] % 2 == 0:
                s -= A[index]

            A[index] += val

            if A[index] % 2 == 0:
                s += A[index]

            queries[i] = s
        return queries
