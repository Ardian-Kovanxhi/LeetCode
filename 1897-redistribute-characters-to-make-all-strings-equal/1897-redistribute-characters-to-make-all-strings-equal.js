/**
 * @param {string[]} words
 * @return {boolean}
 */
var makeEqual = function(words) {
    const logger = {};

    for (let word of words) {
        for (let char of word) {
            if (!logger[char]) logger[char] = 0;
            logger[char]++
        }
    }

    for (let value of Object.values(logger)) {
        if (value%words.length) return false
    }
    return true
};