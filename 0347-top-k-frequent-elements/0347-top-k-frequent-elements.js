/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const logger = {};

    for (let num of nums) {
        if (logger[num]) logger[num]++
        else logger[num] = 1
    }

    const sorted = Object.keys(logger).sort((a,b) => logger[b] - logger[a]);

    return sorted.slice(0,k)
};