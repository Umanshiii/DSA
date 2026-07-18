# http://hackerrank.com/contests/tcs-csac-questions/challenges/array-of-competition/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))

def competition(n,arr):
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            if i==n-2:
                return 'No'
            continue
        else:
            if i==0:
                return 'No'
            start=i
            break
    for i in range(start,n-1):
        if arr[i]>arr[i+1]:
            continue
        else:
            return 'No'
            
    return 'Yes'
    
print(competition(n,arr))