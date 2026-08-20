class Solution:
    def findMin(self, nums: List[int]) -> int:
        target=nums[0]
        for i in range(1,len(nums)):
            target=min(target, nums[i])

        return target


#from binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        while left<right:
            mid=(left+right)//2

            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid

        return nums[left]