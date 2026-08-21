#Word search
#https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def dfs(r,c,k):
            if r<0 or c<0 or c>=n or r>=m or word[k]!=board[r][c]:
                return False
            if k==len(word)-1:
                return True
                
            temp=board[r][c]
            board[r][c]='#'

            found= dfs(r-1,c,k+1) or dfs(r+1,c,k+1) or dfs(r,c+1,k+1) or dfs(r,c-1,k+1)
            board[r][c]=temp
            return found 

        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0] and dfs(r,c,0):
                    return True
                            
        return False