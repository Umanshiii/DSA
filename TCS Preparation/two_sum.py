#Two sum
'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
'''

def twosum(arr, target):
    temp={}
    for i in range(len(arr)):
        if target-arr[i] in temp.keys():
            return [i, temp[target-arr[i]]]
        temp[arr[i]]=i

    # while left<len(arr)-1:
    #     if arr[left]+arr[right]==target:
    #         return [left, right]
    #     if right==len(arr)-1:
    #         left+=1
    #         right=left+1
    #     else:
    #         right+=1
