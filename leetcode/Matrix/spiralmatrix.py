class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out=[]
        
        while matrix:

            out += matrix.pop(0)
            
            for row in matrix:
                if row:
                    out.append(row.pop())

            if matrix:
                out += matrix.pop()[::-1]
            
            for row in matrix[::-1]:
                if row:
                    out.append(row.pop(0))
        
        return out