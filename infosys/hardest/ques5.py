#Shortest Subarray with Sum at Least K

#Sliding window
def subarray(nums,k):
    minlen=float('inf')
    sums=0
    left=0
    for right in range(len(nums)):

        sums+=nums[right]
        while sums>=k:
            minlen=min(minlen,right-left+1)
            sums-=nums[left]
            left+=1            

    return minlen if minlen!=float('inf') else 0

#prefix sum (negetive elements)
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        currsum = 0
        prefix = [0]
        i = 0
        for j in range(len(nums)):
            currsum += nums[j]
            prefix.append(currsum)
        index = deque()
        minlen = float("inf")

        for j in range(len(prefix)):
            while index and prefix[j] - prefix[index[0]] >= k:
                minlen = min(minlen, j - index[0])
                index.popleft()
            while index and prefix[j] <= prefix[index[-1]]:
                index.pop()

            index.append(j)
        
        return -1 if minlen==float('inf') else minlen
