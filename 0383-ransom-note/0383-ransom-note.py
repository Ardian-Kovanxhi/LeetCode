class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        logger = {}

        for c in magazine:
            logger[c] = logger.get(c, 0) + 1
        for c in ransomNote:
            if c not in logger: return False
            elif logger[c] == 1: del logger[c]
            else: logger[c] -= 1
        return True