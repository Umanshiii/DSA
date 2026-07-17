# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/litre-of-milk/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
r1=int(input())
r2=int(input())
r3=int(input())
res=0
if r1<=(r2-r3):
    res=n//r1
else:
    res=(n-r3)//(r2-r3)
    n=n-(res*(r2-r3))
    res+=n//r1
    
print(res)
    