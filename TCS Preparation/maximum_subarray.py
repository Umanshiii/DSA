'''
Given an array of integers and a number $K$, write a complete program from scratch 
to find the maximum sum of any contiguous subarray of size K.

The first line contains the array elements. The second line contains the integer K.
'''

def max_subarray(arr, k):

    tempsum=0

    for i in range(k):
        tempsum+=arr[i]

    maxsum=tempsum

    for i in range(k, len(arr)):
        tempsum+=arr[i]
        tempsum-=arr[i-k]

        if tempsum>maxsum:
            maxsum=tempsum

    return maxsum

arr = list(map(int, input().split()))
k = int(input())
print(max_subarray(arr, k))