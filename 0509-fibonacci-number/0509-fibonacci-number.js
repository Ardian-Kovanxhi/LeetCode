/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n === 0) return 0;
    let prev = 0;
    let curr = 1;
    
    for (let i = 1; i < n; i++) {
        const newNum = prev + curr;
        prev = curr;
        curr = newNum;
    }

    return curr;
};