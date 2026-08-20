#https://leetcode.com/problems/eliminate-maximum-number-of-monsters

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[]
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])
        time.sort()
        count=0
        for i in range(1, len(time)):
            if time[i]<=i:
                return i

        return len(dist)