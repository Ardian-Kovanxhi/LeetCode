/**
 * @param {number[][]} adjacentPairs
 * @return {number[]}
 */
var restoreArray = function(adjacentPairs) {
    //NON ORIGINAL SOLUTION
    //COME BACK LATER WHEN MORE COMFORTABLE WITH GRAPHS
    const ans = [];
    const graph = new Map();

    for (let pair of adjacentPairs) {
        if (!graph.has(pair[0])) graph.set(pair[0], []);
        if (!graph.has(pair[1])) graph.set(pair[1], []);
        graph.get(pair[0]).push(pair[1]);
        graph.get(pair[1]).push(pair[0]);
    }


    for (let [node, neighbors] of graph) {
        if (neighbors.length === 1) {
            ans.push(node);
            ans.push(neighbors[0]);
            break;
        }
    }

    while (ans.length < adjacentPairs.length + 1) {
        const lastElement = ans[ans.length - 1];
        const secondLastElement = ans[ans.length - 2];
        let newEl = graph.get(lastElement);

        if (newEl[0] !== secondLastElement) ans.push(newEl[0]);
        else ans.push(newEl[1]);
    }
    return ans
};