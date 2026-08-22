#Vacation Problem
'''
Andy wants to go on a vacation to de-stress himself. Therefore he decides to take a 
trip to an island. It is given that he has as many consecutive days as possible to 
rest, but he can only make one trip to the island. 

Suppose that the days are numbered from 1 to N. Andy has M obligations in his schedule, 
which he has already undertaken and which correspond to some specific days. This means 
that ith obligation is scheduled for day Di. Andy is willing to cancel at most k of his 
obligations in order to take more holidays.

Your task is to find out the maximum days of vacation Andy can take by canceling at most 
K of his obligations.
'''

n=10
m=5
k=2
arr=[6,9,3,2,7]

def vacation(n,m,k,arr):
    count=0
    ans=0
    arr=set(arr)
    days=[] #[0,1,1,0,0,1,1,0,1,0]

    for i in range(1,n+1):
        if i in arr:
            days.append(1)
        else:
            days.append(0)
    
    left=0
    for right in range(n):
        if days[right]==1:
            count+=1

        while count>k:
            if days[left]==1:
                count-=1
            left+=1
        ans=max(ans,right-left+1)   

    return ans

print(vacation(n,m,k,arr))

#Optimized

def problem(n,m,k,arr):
    if k>=m:
        return n
    arr.sort() #[2,3,6,7,9]
    lis=[arr[0]-1]
    for i in range(1,m):
        lis.append(arr[i]-arr[i-1]-1)
    lis.append(n-arr[m-1]) #[1,0,2,0,1,0]
    ans=lis[0]
    left=0
    for i in range(1,k+1):
        ans+=lis[i]
    maxsum=ans
    for right in range(k+1,len(lis)):
        ans+=lis[right]
        ans-=lis[right-(k+1)]
        maxsum=max(ans,maxsum)

    return maxsum+k