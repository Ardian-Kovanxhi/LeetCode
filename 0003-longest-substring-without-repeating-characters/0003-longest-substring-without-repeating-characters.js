/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length === 1) return 1
    let l = 0;
    let r = 1;
    const strSet = new Set();
    strSet.add(s[l]);
    let longest = 0
    while (r <= s.length) {
        const char = s[r]
        let checked = strSet.has(char);

        if (strSet.size > longest) longest = strSet.size;

        if (checked) {
            while (checked) {
                strSet.delete(s[l]);
                l++;
                checked = strSet.has(char);
            };
            strSet.add(char)
            r++
        } else {
            strSet.add(char);
            r++;
        }

    }
    return longest
};