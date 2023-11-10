/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
     let max = 0;
    let minspeed;

    for (let pile of piles) {
        if (pile > max) max = pile
    }

    if (piles.length === h) return max

    let l = 1;
    let r = max

    while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        let time = 0

        for (let pile of piles) {
            time += Math.ceil(pile / mid)
        }

        if (time <= h) {
            minspeed = mid;
            r = mid - 1;
        }
        else if (time > h) l = mid + 1;
    }

    return minspeed
};