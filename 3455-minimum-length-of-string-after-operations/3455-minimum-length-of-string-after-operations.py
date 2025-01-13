class Solution:
    def minimumLength(self, s: str) -> int:
        logger = defaultdict(int)

        for ch in s:
            logger[ch] += 1
        print(logger)
        diff = 0
        for count in logger.values():
            curr = count
            while curr >= 3:
                curr -= 2
                diff += 2

        return len(s) - diff