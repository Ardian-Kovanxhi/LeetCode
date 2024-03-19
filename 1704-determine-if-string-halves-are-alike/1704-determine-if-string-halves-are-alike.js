/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    const vowels = new Set (['a','e','i','o','u'])

    const half = s.length / 2;
    
    let left = 0;
    let right = 0;

    for (let i = 0; i < half; i++) {
        if (vowels.has(s[i].toLowerCase())) left++;
        if (vowels.has(s[i + half].toLowerCase())) right++;
    }

    return left === right
};