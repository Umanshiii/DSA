'''
Given an array of integers nums and an integer k, 
we want to find the total number of continuous 
subarrays whose elements add up exactly to k.
'''
#Prefix sum
def subarray(nums, k):
    hashset={0:[-1]}
    currsum=0
    result = []

    for i in nums:
        currsum+=i
        if (currsum - k) in hashset:
            for start in hashset[currsum - k]:
                result.append(nums[start+1:i+1])

        if currsum in hashset:
            hashset[currsum].append(i)
        else:
            hashset[currsum]=[1]
            
    return result

# Sliding window (only for positive numbers)
def subarray_sum(nums,k):
    start=0
    currsum=nums[0]
    for i in range(1, len(nums)):
        if currsum==k:
            return nums[start:i]
        elif currsum>k:
            currsum=currsum-nums[start] 
            start+=1
        else:
            currsum+=nums[i]
    

# When count is asked 
def subarraySum(self, nums: List[int], k: int) -> int:
    hashset={0:1}
    currsum=0
    count = 0

    for i in nums:
        currsum+=i
        if (currsum - k) in hashset:
            count += hashset[currsum-k]

        if currsum in hashset:
            hashset[currsum]+=1
        else:
            hashset[currsum]=1
                
    return count