class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        logger = {}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in logger: return [i, logger[rem]]
            logger[num] = i