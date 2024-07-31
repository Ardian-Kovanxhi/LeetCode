class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aint = int(a, 2)
        bint = int(b, 2)
        return bin(aint + bint)[2:]