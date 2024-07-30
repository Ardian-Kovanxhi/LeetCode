class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        logger = {}

        i = 0

        while i < len(ransomNote) or i < len(magazine):
            if i < len(ransomNote):
                ranCh = ransomNote[i]
                logger[ranCh] = logger.get(ranCh, 0) - 1

            if i < len(magazine):
                magCh = magazine[i]
                logger[magCh] = logger.get(magCh, 0) + 1

            i += 1
        
        for val in logger.values():
            if val < 0: return False
        return True