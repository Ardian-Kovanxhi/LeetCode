class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        logger = set()

        for i in nums:
            if i in logger: return True
            logger.add(i)
        return False