# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/consecutive-character-1/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

s=input()
def string(s):
    if not s:
        return 0
    hashset={s[0]:1}
    result=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            if s[i] in hashset:
                hashset[s[i]]+=1
        else:
            if hashset[s[i-1]]%2==0:
                result+=hashset[s[i-1]]
            del hashset[s[i-1]]
            hashset[s[i]]=1
            
    if hashset[s[-1]]%2==0:
        result+=hashset[s[-1]]
           
    return result     
        
print(string(s))