class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        for i in range(1, length):
            ans[i] *= ans[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                postfix *= nums[i]
            else:
                ans[i] *= postfix
                postfix *= nums[i]
        return ans