# number of islands
# http://leetcode.com/problems/number-of-islands/submissions/2114156230/?envType=problem-list-v2&envId=dx0zby06&

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r>=m or r<0 or c<0 or c>=n or grid[r][c]!='1':
                return
            
            grid[r][c]='0'

            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
        
        count=0
        m,n=len(grid),len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1':
                    count+=1
                    dfs(r,c)
                
        return count
                