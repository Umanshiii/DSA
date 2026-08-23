#Good nodes

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0

        def good(node,maxval):
            nonlocal count
            if not node:
                return 0
            if node.val>=maxval:
                maxval=node.val
                count+=1

            left=good(node.left,maxval)
            right=good(node.right,maxval)

            return 

        good(root, root.val)
        return count