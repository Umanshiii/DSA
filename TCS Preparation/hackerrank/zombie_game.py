#https://www.hackerrank.com/contests/tcs-csac-questions/challenges/zombie-world-game/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

inp=list(map(int, input().split()))
n=inp[1]
b=inp[0]
zi=list(map(int, input().split()))

def energy(n,b,zi):
  zi.sort(reverse=True)
  for i in range(n):
    if b<zi[i]:
      return 'NO'
    b-=(zi[i]%2)+(zi[i]/2)
    
  return 'YES'
  
print(energy(n,b,zi))