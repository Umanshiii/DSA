'''
Find an index in an array such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. 
If no such index exists, return -1.
'''
import sys
arr=list(map(int,input().split()))

def equilibrium(arr):
    leftsum=0
    rightsum=0
    for i in range(1,len(arr)):
        rightsum+=arr[i]
    if leftsum==rightsum:
        return 0
    for i in range(1,len(arr)):
        leftsum+=arr[i-1]
        rightsum-=arr[i]
        if leftsum==rightsum:
            return i

    return -1