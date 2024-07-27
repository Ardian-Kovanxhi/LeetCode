class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sLogger = {}
        tLogger = {}

        for i in range(len(s)):
            sLogger[s[i]] = sLogger.get(s[i], 0) + 1
            tLogger[t[i]] = tLogger.get(t[i], 0) + 1
        
        return sLogger == tLogger
