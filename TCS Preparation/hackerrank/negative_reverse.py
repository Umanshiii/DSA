# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/serious-issue-with-numbers/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
def func(n):
    res=''
    if -32768<n<32767:
        if n==0: 
            return 0
        negative=n<0
        n = abs(n)
        
        while n>0:
            res+=str(n%10)
            n=n//10
    else:
        return 'Wrong value'

    return -int(res) if negative else int(res)
    
print(func(n))