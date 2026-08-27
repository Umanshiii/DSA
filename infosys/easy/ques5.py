#Tree beauty problem
'''
You are given a tree of n nodes, each node has a value a[i] written on it. 
The tree is rooted at node 1.
A pair of nodes i, j (where 1 ≤ i < j ≤ n) is considered GOOD if a[i]×a[j] is a perfect square.
We define beauty(u) as the number of good pairs of nodes in the subtree of u. Your task is to
find the sum of beauty(i) for each 1 ≤ i ≤ n. Return the sum of these values modulo 109 + 7.
'''

def get_ans(n,par,a):
    def dfs(node):
        if not node:
            return 0
        
        left=dfs(node.left)
        right=dfs(node.right)

        temp=int((left.val*right.val)**0.5)

        return temp*temp==left.val*right.val