'''
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one. You must implement a solution with a linear runtime complexity O(N)
and use only constant extra space O(1).

If we had an array like nums=[4, 1, 2, 1, 2], output=4 
because it's the only number that doesn't have a pair.
'''
def single(nums):
    result=nums[0]
    for i in range(len(nums)):
        result=result^nums[i-1]
    return result