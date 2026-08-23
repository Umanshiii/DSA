# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        def depth(n):
            if n==None:
                return 0
            
            return 1+max(depth(n.left),depth(n.right))
        if not root:
            return 0
            
        return 1+max(depth(root.left),depth(root.right))
