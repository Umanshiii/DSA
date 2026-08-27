class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        n=len(s)
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            if len(s[left + 1 : right]) > len(res):
                res=s[left+1:right]
            left,right=i,i+1
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            if len(s[left + 1 : right]) > len(res):
                res = s[left + 1 : right]

        return res
            