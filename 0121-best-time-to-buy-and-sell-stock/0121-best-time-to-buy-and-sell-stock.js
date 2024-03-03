/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
    let maxProfit = 0;
    
    let l = 0;
    let r = 1;

    while (r < prices.length) {
        const left = prices[l];
        const right = prices[r];

        if (right < left) {
            l = r;
            r++;
            continue;
        }

        const curr = right - left;
        maxProfit = Math.max(maxProfit, curr);
        r++;
    }

    return maxProfit;
};