/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false
    const sLogger = {};
    const tLogger = {};
    for (let i = 0; i < s.length; i++) {
        const sChar = s[i];
        const tChar = t[i];

        if (sLogger[sChar]) {
            sLogger[sChar]++;
        }
        else sLogger[sChar] = 1;

        if (tLogger[tChar]) {
            tLogger[tChar]++;
        }
        else tLogger[tChar] = 1;
    }
 
    for (let char of Object.keys(sLogger)) {
        if (sLogger[char] === tLogger[char]) continue
        return false
    }
    return true
};