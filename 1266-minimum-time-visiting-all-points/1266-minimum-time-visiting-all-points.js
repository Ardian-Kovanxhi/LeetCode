/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let time = 0;
    for (let i = 1; i < points.length; i++) {
        const prev = points[i - 1];
        const curr = points[i];
        const x = Math.abs(curr[0] - prev[0]);
        const y = Math.abs(curr[1] - prev[1]);
        if (x < y) time += y;
        else time += x;
    }
    return time;
};