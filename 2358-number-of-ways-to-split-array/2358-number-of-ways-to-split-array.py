class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        length = len(nums)
        leftSum = [0] * (length - 1)
        rightSum = [0] * (length - 1)

        for i in range(length - 1):
            if i == 0:
                leftSum[i] = nums[i]
            else:
                leftSum[i] = leftSum[i - 1] + nums[i]

        count = 0
        for i in range(-1, -length, -1):
            if i == -1:
                rightSum[i] = nums[i]
            else:
                rightSum[i] = nums[i] + rightSum[i + 1]

            if leftSum[i] >= rightSum[i]: count += 1
        
        return count