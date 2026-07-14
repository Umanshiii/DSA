# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/find-the-number-of-ways-1-1/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

N=int(input())
M=int(input())
P=int(input())
E=int(input())

def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)

def func(N,M,P,E):
  pencils=fact(N)//(fact(P)*fact(N-P))
  erasers=fact(M)//(fact(E)*fact(M-E))
  ways=pencils*erasers
  
  return ways

print(func(N,M,P,E))