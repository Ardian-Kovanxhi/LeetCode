/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    const sLogger = {};
    const tLogger = {};

    for (let i = 0; i < s.length; i++) {
        if (!sLogger[s[i]]) sLogger[s[i]] = 1;
        else sLogger[s[i]]++;
        if (!tLogger[t[i]]) tLogger[t[i]] = 1;
        else tLogger[t[i]]++;
    };
    for (let key of Object.keys(sLogger)) {
        if (!tLogger[key]) return false;
        if (sLogger[key] !== tLogger[key]) return false;
    };
    return true;
};