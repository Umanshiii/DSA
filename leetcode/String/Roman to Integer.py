class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        out = dic[s[-1]]
        
        i = len(s) - 2
        
        while i >= 0:
            if dic[s[i]] < dic[s[i+1]]:
                out -= dic[s[i]]
            else:
                out += dic[s[i]]
            
            i -= 1
            
        return out
        
