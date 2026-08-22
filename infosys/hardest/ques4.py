#Gym Energy Depletion

'''
Today you decided to go to the gym. You currently have energy equal to E units. 
There are N exercises in the gym. Each of these exercises drains Ai amount of 
energy from your body.

You feel tired if your energy reaches 0 or below. Calculate the minimum number 
of exercises you have to perform such that you become tired. Every unique exercise 
can only be performed at most 2 times as others also have to use the machines.

If performing all the exercises does not make you feel tired, return -1
'''

def gym(e,n,arr):
    arr.sort(reverse=True)
    i=0
    count=0
    while e>0:
        for _ in range(2):
            e-=arr[i]
            count+=1
            if e<=0:
                return count
        i+=1
        if i==len(arr):
            return -1
            
    return count