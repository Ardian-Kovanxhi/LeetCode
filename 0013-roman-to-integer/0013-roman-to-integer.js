/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const romNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000};

    let total = 0;

    for (let i = 0; i < s.length; i++) {
        const curr = s[i];

        if (romNum[curr] < romNum[s[i + 1]]) total -= romNum[curr];
        else total += romNum[curr];
    }


    return total;
};