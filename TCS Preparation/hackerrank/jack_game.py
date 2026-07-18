# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/jack-game/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n=int(input())
arr=list(map(int,input().split()))
visited=[False]*n
ans=1
for i in range(len(arr)):
    if not visited[i]:
        index=i
        cycle=0
    while not visited[index]:
        visited[index]=True
        index=arr[index]-1
        cycle+=1
    ans=(ans*cycle) // math.gcd(ans, cycle)
    
print(ans)