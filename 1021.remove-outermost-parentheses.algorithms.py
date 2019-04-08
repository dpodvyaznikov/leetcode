class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        balance = 0
        start = None
        output = ''
        for i, symbol in enumerate(S):
            if symbol == '(':
                balance += 1
                if start is None:
                    start = i
            if symbol == ')':
                balance -= 1
            if balance == 0:
                output += S[start+1:i]
                start = None
        return output