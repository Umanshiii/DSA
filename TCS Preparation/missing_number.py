#Missing Number
'''
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''

def dup(nums):
    n=len(nums)
    total=0
    arraysum=n*(n+1)//2
    for i in nums:
        total+=i

    return arraysum-total
