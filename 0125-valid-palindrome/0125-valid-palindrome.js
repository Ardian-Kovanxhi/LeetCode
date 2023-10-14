/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.replace(/[^a-z0-9]/gi, '').toLowerCase()

    let l = -1;
    let r = s.length;

    while (l++ <= r--) {
        if (s[l] !== s[r]) return false
    }

    return true
};