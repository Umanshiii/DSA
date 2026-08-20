'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        for i in range(1,n):
            if n//((5)**i)<1:
                break
            ans+=n//((5)**i)

        return ans