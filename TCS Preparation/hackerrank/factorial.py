# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/play-with-numbers-14/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())

def fact(n):
    ans=1
    while n>0:
        ans*=n
        n-=1

    while ans%10==0:
        ans=ans//10

    return ans%10

print(fact(n))