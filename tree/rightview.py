# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = [root]
        front = 0
        res = []
        
        while front < len(q):
            level_size = len(q) - front
            level = []
            
            for _ in range(level_size):
                node = q[front]
                front += 1
                
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        
        out=[l[-1] for l in res]
        return out