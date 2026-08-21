#Number of enclaves
#https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!=1:
                return
            
            grid[r][c]=0

            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)

        m,n=len(grid),len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r==0 or r==m-1 or c==0 or c==n-1) and grid[r][c]==1:
                    dfs(r,c)
        count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    count+=1

        return count