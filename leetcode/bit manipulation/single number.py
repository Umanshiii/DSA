class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                if i==1:
                    return nums[0]
                if i==len(nums)-1:
                    return nums[i]
                else:
                    if nums[i]!=nums[i+1]:
                        return nums[i]
                    else:
                        continue
