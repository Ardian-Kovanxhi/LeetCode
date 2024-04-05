public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.Length - 1;

        int[] ans = new int[2];

        while (l <= r) {
            int sum = numbers[l] + numbers[r];

            if (sum == target) {
                ans[0] = l + 1;
                ans[1] = r + 1;
                return ans;
            }
            else if (sum < target) l++;
            else r--;
        }
        return ans;
    }
}