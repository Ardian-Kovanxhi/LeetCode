class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        logger = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in logger: return [logger[diff], i]
            logger[v] = i