class Solution:
    def maxScore(self, s: str) -> int:
        max_sum = 0
        one_sum = 0
        for c in s:
            if c == "1":
                one_sum += 1

        zero_sum = 0
        for i in range(len(s) - 1):
            curr = s[i]
            if curr == "0":
                zero_sum += 1
            elif curr == "1":
                one_sum -= 1

            max_sum = max(max_sum, zero_sum + one_sum)
        return max_sum