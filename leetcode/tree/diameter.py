# Diameter of binary tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxd=0
        def diameter(node):
            nonlocal maxd
            if not node:
                return 0
            
            left=diameter(node.left)
            right=diameter(node.right)

            maxd=max(maxd,left+right)

            return 1+max(right,left)
        
        diameter(root)
        return maxd