'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    right = 0
    sums = 0
    length = float('inf')
    n = len(nums)        
    while right < n:
        sums += nums[right]    
        while sums >= target:
            length = min(length, right - left + 1)
            sums -= nums[left]
            left += 1    
        right += 1    
    return 0 if length == float('inf') else length
