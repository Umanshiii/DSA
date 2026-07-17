# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/event-management-4/problem?isFullScreen=true

#  Enter your code here. Read input from STDIN. Print output to STDOUT1
s=input()
res=''
for i in range(len(s)):
  if s[i]=='E':
    if s[i+1]=='F':
      continue
  if s[i]=='F':
    if s[i-1]=='E':
      continue
  if s[i]=='G':
    continue
  res+=s[i]
print(res)
      