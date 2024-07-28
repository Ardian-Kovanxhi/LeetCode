class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            print(s[l], s[l].isalnum())
            print(s[r], s[r].isalnum())
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True