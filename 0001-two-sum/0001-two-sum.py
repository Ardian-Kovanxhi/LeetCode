class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        logger = {}
        for i in range(len(nums)):
            num = nums[i]
            rem = target - num
            if rem in logger:
                return [logger[rem], i]
            logger[num] = i