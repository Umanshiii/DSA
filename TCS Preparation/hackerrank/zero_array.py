#https://www.hackerrank.com/contests/tcs-csac-questions/challenges/zero-array-2/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int, input().split()))
def zero(arr,n):
  arrand=arr[0]
  for i in range(1,n):
    arrand=arrand & arr[i]
  if arrand==0:
    return 0
  
  return arrand.bit_count()
  
print(zero(arr,n))
