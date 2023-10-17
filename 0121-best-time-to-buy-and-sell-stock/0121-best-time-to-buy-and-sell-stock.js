/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let l = 0;
    let r = 1;
    let max = 0;

    while (r < prices.length) {
        const sum = prices[r] - prices[l];
        if (sum > max) max = sum
        else if (sum < 0) {
            l = r
            r++
        }
        else r++
    }
    return max
};