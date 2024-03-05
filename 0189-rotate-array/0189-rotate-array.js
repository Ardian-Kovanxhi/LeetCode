/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let dividend = k % nums.length;

    if (dividend === 0) return nums;
    else dividend = k - (Math.floor(k / nums.length) * nums.length);

    const ans = [];

    let i = 0;
    let j = nums.length - dividend;

    while (i < nums.length) {
        ans.push(nums[i]);

        if (j >= nums.length) nums[i] = ans[j - nums.length];
        else {
            nums[i] = nums[j];
        }
        i++;
        j++;
    };
};