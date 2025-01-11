class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        logger = Counter(s)

        loose = 0
        for v in logger.values():
            if v < 2 or v % 2 > 0:
                loose += 1
        if loose > k:
            return False
        return True