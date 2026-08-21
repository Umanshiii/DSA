#Surrounded region
#https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!='O':
                return

            board[r][c]='S'

            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
            
        m=len(board)
        n=len(board[0])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r==0 or c==0 or r==m-1 or c==n-1 and board[r][c]=='O':
                    dfs(r,c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='S':
                    board[r][c]='O'

