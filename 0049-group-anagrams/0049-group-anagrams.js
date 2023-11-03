/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const hashLogger = {};
    //a = 97
    for (let str of strs) {
        const lower = str.toLowerCase();
        const hash = new Array(26).fill(0)
        for (let char of lower) {
            hash[char.charCodeAt(0) - 97]++
        }
        if (!hashLogger[hash]) hashLogger[hash] = [str];
        else hashLogger[hash].push(str)
    }
    return Object.values(hashLogger)
};