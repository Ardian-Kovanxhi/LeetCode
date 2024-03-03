/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length === 0) return 0;

    let l = 0;
    let r = 1;

    let logger = new Set();
    logger.add(s[l]);

    let longest = 1;

    while (r <= s.length) {
        if (logger.size > longest) longest = logger.size;

        let char = s[r];
        let checked = logger.has(s[r]);

        if (checked) {
            while (checked) {
                logger.delete(s[l]);
                l++;
                checked = logger.has(s[r]);
            }
            logger.add(char);
            r++;
        }
        else {
            logger.add(char);
            r++;
        }
    }

    return longest;
};