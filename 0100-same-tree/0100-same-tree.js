/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (p !== null && q !== null) {
        if (p.val === q.val) console.log('we good');
        else return false;
    }
    else if (p === null && q === null) return true;
    else return false;

    const right = isSameTree(p.right, q.right);
    const left = isSameTree(p.left, q.left);

    if (right && left) return true
    else return false
};