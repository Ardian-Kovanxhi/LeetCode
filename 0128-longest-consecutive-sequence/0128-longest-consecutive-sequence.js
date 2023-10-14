/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0) return 0
    nums.sort((a,b) => a - b);

    const logger = [];

    let counter = 1;

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const next = nums[i + 1];

        if (num === next) continue;
        if (num + 1 === next) counter++;
        else {
            logger.push(counter);
            counter = 1;
        };
    }

    return logger.sort((a,b) => b - a)[0];
    
};