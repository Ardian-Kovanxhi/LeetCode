/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    if (n === 1) return 1
    const logger = {};

    for (let rel of trust) {
        if (!logger[rel[0]]) logger[rel[0]] = [0,0];
        if (!logger[rel[1]]) logger[rel[1]] = [0,0];
        logger[rel[0]][1]++;
        logger[rel[1]][0]++;
    };

    for (let key of Object.keys(logger)) {
        if (logger[key][0] === n - 1 && logger[key][1] === 0) return key;
    };

    return -1;
};