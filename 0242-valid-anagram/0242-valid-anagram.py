class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_logger = {}
        t_logger = {}

        for i in range(len(s)):
            s_logger[s[i]] = 1 + s_logger.get(s[i], 0)
            t_logger[t[i]] = 1 + t_logger.get(t[i], 0)
        
        return s_logger == t_logger