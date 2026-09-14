class Solution:
    def reverse(self, x: int) -> int:
        out=[]
        for i in range(len(str(x))-1,-1,-1):
            if str(x)[i]=='-':
                out.insert(0,'-')
            else:
                out.append(str(x)[i])

        result = int(''.join(out))
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result