class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        res = 0

        for count in counter.values():
            if count < 3:
                res += count
            elif count % 2 == 0:
                res += 2
            else:
                res += 1

        return res