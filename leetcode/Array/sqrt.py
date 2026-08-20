class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        ans=0
        for i in range(1,x+1):
            if i*i==x:
                return i
            elif i*i<x:
                ans=i
            else:
                break

        return ans