class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        logger = set()

        for num in nums:
            if num in logger: return True
            logger.add(num)
        return False