class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        s=''
        for i in range(len(str(x))-1,-1,-1):
            s+=str(x)[i]
        if int(s)==x:
            return True
        else:
            return False