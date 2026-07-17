# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/shopkeeper-transaction/problem?isFullScreen=true
 
# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))  
def shop(n,arr):
  cash=0
  for i in arr:
    if i%30!=0:
      return 'Transaction failed'
    if i==30:
      cash+=i
    if i>30 and cash<i-30:
      return 'Transaction failed'
    if cash<i:
      return 'Transaction failed'
    cash+=i
  return 'Transaction successful'
  
print(shop(n,arr))
    
      