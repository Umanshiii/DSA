# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/pizza-party-4/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

first=list(map(int, input().split()))
n=first[0]
k=first[1]
arr=list(map(int, input().split()))

def func(arr,n,k):
  hashset={}
  left=0
  maxlen = 0
  for right in range(n):
    if arr[right] in hashset:
      hashset[arr[right]]+=1
    else:
      hashset[arr[right]]=1
      while len(hashset)>k-1:
        hashset[arr[left]]-=1
        if hashset[arr[left]]==0:
          del hashset[arr[left]]
        left+=1
    maxlen = max(right-left+1, maxlen)
  
  return maxlen
    
print(func(arr,n,k))