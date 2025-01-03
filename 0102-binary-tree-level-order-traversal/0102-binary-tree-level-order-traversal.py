# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        queue = [root]
        temp = []
        i = 0

        while queue:
            if i == len(queue):
                ans.append(queue)
                queue = temp
                temp = []
                i = 0
            else:
                curr = queue[i]
                if curr.left: temp.append(curr.left)
                if curr.right: temp.append(curr.right)
                queue[i] = curr.val
                i += 1
        return ans