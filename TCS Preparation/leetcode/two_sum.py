#Two sum
'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
'''
# o(n)
def twosum(arr, target):
    temp={}
    for i in range(len(arr)):
        if target-arr[i] in temp.keys():
            return [i, temp[target-arr[i]]]
        temp[arr[i]]=i

# O(1)
# Sorted array
def two_sum(arr, target):
    left=0
    right=len(arr)-1
    result=0
    while left<right:
        if arr[left]+arr[right]==target:
            return [arr[left],arr[right]]
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right-=1

    return "No pair found"
