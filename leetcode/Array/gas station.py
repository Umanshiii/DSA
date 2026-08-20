class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        curr = 0
        ans = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            
            total += diff
            curr += diff
            
            if curr < 0:
                ans = i + 1
                curr = 0
        
        if total < 0:
            return -1
        
        return ans
                
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))