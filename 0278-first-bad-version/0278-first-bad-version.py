# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        source = float("inf")
        while l <= r:
            mid = (l + r) // 2
            check = isBadVersion(mid)
            if check:
                source = min(mid, source)
                r = mid - 1
            else: l = mid + 1
        return source



