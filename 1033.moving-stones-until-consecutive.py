class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        l = [a, b, c]
        l.sort()
        a, b, c = l
        delta1, delta2 = b-a, c-b
        print(delta1, delta2)
        if delta1 == 1 and delta2 == 1:
            return [0,0]
        elif delta1 == 1 or delta1 == 2:
            return [1, delta1+delta2-2]
        elif delta2 == 1 or delta2 == 2:
            return [1, delta1+delta2-2]
        else:
            return [2, delta1+delta2-2]
