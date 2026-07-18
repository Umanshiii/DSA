# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/string-sorting-15/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

s=input()
key=input()
res=''
hashset={}
for i in s:
    if i in hashset:
        hashset[i]+=1
    else:
        hashset[i]=1
for i in key:
    if i in hashset:
        res+=(i*hashset[i])

print(res)