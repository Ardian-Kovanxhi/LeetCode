/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(nums, queries) {
    let evenTotal = 0;

    for (let num of nums) {
        if (num % 2 === 0) evenTotal += num;
    }

    const ans = [];

    for (let query of queries) {
        
        if (nums[query[1]] % 2 === 0) evenTotal -= nums[query[1]];

        nums[query[1]] = nums[query[1]] + query[0];

        if (nums[query[1]] % 2 === 0) evenTotal += nums[query[1]];

        ans.push(evenTotal);
    }

    return ans
};