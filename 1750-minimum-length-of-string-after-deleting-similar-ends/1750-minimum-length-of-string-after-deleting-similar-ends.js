/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    let l = 0;
    let r = s.length - 1;
    
    let curr;

    while (l <= r) {

        if (l === r && s[l] !== curr) return 1

        if (s[l] === s[r] && s[l] !== curr) {
            curr = s[l];
            console.log(l)
            console.log(r)
            console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        }

        if (s[l] !== curr && s[r] !== curr) break;
        if (s[l] === curr) l++;
        if (s[r] === curr) r--;

    }

    console.log(l)
    console.log(r)

    return Math.max(r - l + 1, 0)
};