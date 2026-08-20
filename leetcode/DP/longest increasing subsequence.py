class Solution:
    def low(self,lis,num):
        start=0
        end=len(lis)-1
        ans=len(lis)
        while start<=end:
            mid=(start+end)//1
            if lis[mid]>=num:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans

    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[nums[0]]
        
        for i in range(1,n):
            if nums[i]>lis[-1]:
                lis.append(nums[i])
            else:
                lb=self.low(lis,nums[i])
                lis[lb]=nums[i]

        return len(lis)