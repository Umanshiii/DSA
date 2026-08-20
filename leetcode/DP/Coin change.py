'''
Given an amount and the denominations of coins available, determine how many ways
change can be made for amount. There is a limitless supply of each coin type.

Example
n=3
c = [8,3, 1, 2]

There are 3 ways to make change for n = 3: {1, 1, 1}, {1, 2}, and {3}.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = [amount + 1] * (amount + 1)
        m[0] = 0

        for i in coins:
            for j in range(i, amount + 1):
                m[j] = min(m[j],m[j - i]+ 1)

        count = m[amount]
        return count if count<=amount else -1
