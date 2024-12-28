class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        logger = set(list(jewels))
        count = 0
        for i in stones:
            if i in logger: count += 1
        return count