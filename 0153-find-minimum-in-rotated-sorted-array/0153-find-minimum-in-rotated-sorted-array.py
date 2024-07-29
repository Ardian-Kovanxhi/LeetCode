class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]

        l, r = 0, len(nums) - 1

        curr_min = float("inf")

        while l <= r:
            mid = (l + r) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

            
        return min(curr_min, nums[r])