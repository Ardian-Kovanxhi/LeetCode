class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        logger = {}
        half = len(nums) // 2

        for num in nums:
            logger[num] = logger.get(num, 0) + 1
            if logger[num] > half: return num