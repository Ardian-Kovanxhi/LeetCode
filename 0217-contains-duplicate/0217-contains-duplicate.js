/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const logger = {};
    for (let num of nums) {
        if (logger[num]) return true;
        logger[num] = true;
    };
    return false;
};