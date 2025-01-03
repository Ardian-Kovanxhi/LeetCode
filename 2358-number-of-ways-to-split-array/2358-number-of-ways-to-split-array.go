func waysToSplitArray(nums []int) int {
	ans := 0
	left_sum := 0
	total := 0

	for i := 0; i < len(nums); i++ {
		total += nums[i]
	}
	for i := 0; i < len(nums)-1; i++ {
		left_sum += nums[i]
		right_sum := total - left_sum

		if left_sum >= right_sum {
			ans++
		}
	}

	return ans
}