class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        logger = {}

        for num in nums:
            logger[num] = logger.get(num, 0) + 1

            if logger[num] == math.ceil(len(nums) / 2): return num