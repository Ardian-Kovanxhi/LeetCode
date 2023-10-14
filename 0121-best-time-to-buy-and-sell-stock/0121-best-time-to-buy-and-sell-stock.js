/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minCostInd = 0;
    let maxCostInd = 0;
    let tempMinInd

    for (let i = 0; i < prices.length; i++) {
        const val = prices[i];
        const minVal = prices[minCostInd];
        const maxVal = prices[maxCostInd];

        if (val - prices[tempMinInd] > maxVal - minVal) {
            minCostInd = tempMinInd
            maxCostInd = i
        }

        if (maxCostInd && val < minVal) {
            if (tempMinInd && prices[tempMinInd] < val) {
                continue
            }
            tempMinInd = i
            continue
        }

        if (val < minVal) {
            minCostInd = i;
            if (!maxCostInd || maxCostInd < i) maxCostInd = i
        }

        if (i > minCostInd && val > maxVal) maxCostInd = i
    };
    return prices[maxCostInd] - prices[minCostInd]
};

// var maxProfit = function(prices) {
//     let maxProfit = 0;
//     let minPrice = prices[0];
//     for (let i = 1; i < prices.length; i++) {
//         const currentPrice = prices[i];
//         const currentProfit = currentPrice - minPrice;
//         if (currentProfit > maxProfit) {
//             maxProfit = currentProfit;
//         }
//         if (currentPrice < minPrice) {
//             minPrice = currentPrice;
//         }
//     }
//     return maxProfit;
// };