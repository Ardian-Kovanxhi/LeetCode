class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        a_set = set()
        b_set = set()
        total = 0
        for i in range(n):
            currA = A[i]
            currB = B[i]
            a_set.add(currA)
            b_set.add(currB)
            if currB in a_set: total += 1
            if currA in b_set: total += 1
            if currA == currB: total -= 1
            res[i] = total
        return res

