# http://hackerrank.com/contests/tcs-csac-questions/challenges/person-is-travelling/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

h=int(input())
m=int(input())

def cal(h,m):
  if h > 24:
    return ((h - 24) * 60) + m
  if h == 24 and m > 0:
    return -m
      
  if m==0:
    h=24-h
    m=0
  elif m>0:
    h=23-h
    m=60-m
    
  return f'{h:02d}::{m:02d}'
  
print(cal(h,m))
