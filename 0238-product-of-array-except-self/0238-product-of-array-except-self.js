/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const res = [];
   
   for (let i = 0; i < nums.length; i++) {

       if (i === 0) {
           res.push(1);
           continue;
       }

       res.push(res[i - 1] * nums[i - 1])

   }

   let post

   for (let i = nums.length - 1; i >= 0; i--) {
       if (i === nums.length - 1) {
           post = nums[i]
           continue
       }

       res[i] *= post
       post *= nums[i]
   }

    return res
};