'''
A gym offers different membership plans based 
on the number of months a customer signs up for:  
12 months = ₹15,000  
9 months = ₹12,000  
6 months = ₹9,000  
3 months = ₹5,000  
Given an integer $N$ representing the total number 
of months a person wants to join, calculate the 
minimum total cost using a greedy strategy.  

The Priority Rule: You must always try to fit the largest possible package first.  

Constraint: If the number of months N is not perfectly divisible by 3, the gym 
cannot offer a plan for those exact months, so you must print "Error".

'''

def gym_fees(n):
    dic={12:15000, 9:12000, 6:9000, 3:5000}
    if n%3!=0:
        return "Error"
    cost=0
    for i,j in dic.items():
        while n>=i:
            n-=i
            cost+=j
    return cost

print(gym_fees(24))