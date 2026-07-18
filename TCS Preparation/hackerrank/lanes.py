# https://www.hackerrank.com/contests/tcs-csac-questions/challenges/lanes-of-city/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

def vehicles(n,a,b,c,d):
    l1=set()
    for i in range(n):
        l1.add(b+(i*a))
    for i in range(n):
        l2=d+(i*c)
        if l2 in l1:
            return l2
    return 'No same amount of fuel found'
        
print(vehicles(n,a,b,c,d))

