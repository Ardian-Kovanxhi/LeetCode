class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        diff = 0
        for count in counter.values():
            curr = count
            while curr > 2:
                curr -= 2
                diff += 2

        return len(s) - diff