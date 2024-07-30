# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]
        checker = set([p, q])
        currRoot = None


        while queue:
            curr = queue.pop(0)
            if not currRoot and p.val < curr.val < q.val or q.val < curr.val < p.val: return curr
            if curr in checker:
                if currRoot: return currRoot
                currRoot = curr
                
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
