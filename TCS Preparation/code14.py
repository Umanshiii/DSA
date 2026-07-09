#Numbers Disappeared Array
'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''

def disappeared(arr):
    result=[]
    n=len(arr)
    for i in arr:
        index = abs(i)-1
        if arr[index]>0:
            arr[index]=-arr[index]
    for i in range(n):
        if arr[i]>0:
            result.append(i+1)

    return result