/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    let newStr = '';

    let spaceInd = 0;

    for (let i = 0; i < s.length; i++) {
        if (i === spaces[spaceInd]) {
            spaceInd++;
            newStr += ` ${s[i]}`;
        }
        else newStr += s[i];
    }

    return newStr
};