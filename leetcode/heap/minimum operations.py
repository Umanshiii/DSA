'''
You are given a 0-indexed integer array nums, and an integer k.

You are allowed to perform some operations on nums, where in a single operation, you can:

Select the two smallest integers x and y from nums.
Remove x and y from nums.
Insert (min(x, y) * 2 + max(x, y)) at any position in the array.
Note that you can only apply the described operation if nums contains at least two elements.
'''

import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        heapq.heapify(nums)
        while nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            heapq.heappush(nums, x*2+y)
            count+=1
        return count
            
        