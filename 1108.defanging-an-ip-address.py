class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace('.', '[.]')
        # return '[.]'.join(address.split('.'))
        return ''.join([s if s!='.' else '[.]' for s in address])