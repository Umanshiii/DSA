#Nearest Exit from Entrance in Maze
#https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])

        maze[entrance[0]][entrance[1]]='+'

        direct=[(-1,0),(0,1),(1,0),(0,-1)]
        queue=[(entrance[0],entrance[1],0)]
        head=0

        while head<len(queue):
            r,c,dist=queue[head]
            head+=1
            for dr,dc in direct:
                nr,nc= r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and maze[nr][nc]=='.':
                    if nr==m-1 or nc==n-1 or nr==0 or nc==0:
                        return dist+1
                    else:
                        queue.append((nr,nc,dist+1))
                        maze[nr][nc]='+'

        return -1