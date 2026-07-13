'''
A shopkeeper has a single bag that can hold a maximum weight 
of W kg. There are several items available, each with a specific 
total value (profit) and a total weight.

To maximize profit, the shopkeeper wants to fill the bag such that 
the total value is as high as possible. Unlike some problems where 
you must take a whole item, here you can break items into smaller 
fractions if the whole item doesn't fit.
'''
# Max capacity of bag (W): 50 kg
# Items available:
# Item 1: Value = 60, Weight = 10 kg
# Item 2: Value = 100, Weight = 20 kg
# Item 3: Value = 120, Weight = 30 kg

class Solution:
    def fractionalKnapsack(self, val, wt, w):
        #code here
        items= list(zip(val, wt))
        items.sort(key=lambda x: x[0]/x[1], reverse=True)
        bag=0
        profit=0
        for i in items:
            if i[1]+bag<w:
                bag+=i[1]
                profit+=i[0]
            else:
                remaining=w-bag
                profit+=remaining*(i[0]/i[1])
                break
        return profit
