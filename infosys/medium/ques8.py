#Rotten oranges
#https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh=0
        rotten=[]

        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        if fresh==0:
            return 0

        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        head=0
        time=0

        while head<len(rotten) and fresh>0:
            elements=len(rotten)-head
            time+=1
            for _ in range(elements):
                r,c=rotten[head]
                head+=1
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        rotten.append((nr,nc))
                        fresh-=1
            
        if fresh==0:
            return time
        elif fresh>0:
            return -1