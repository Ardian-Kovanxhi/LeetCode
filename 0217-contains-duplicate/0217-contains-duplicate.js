/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const logger = new Set();
    for (let num of nums) {
        if (logger.has(num)) return true;
        logger.add(num);
    };
    return false;
};