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
        stack = [root]
        temp = []
        i = 0

        while stack:
            print(i)
            if i == len(stack):
                ans.append(stack)
                stack = temp
                temp = []
                i = 0
            else:
                curr = stack[i]
                if curr.left: temp.append(curr.left)
                if curr.right: temp.append(curr.right)
                stack[i] = curr.val
                i += 1
        return ans