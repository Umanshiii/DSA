#longest stretch of consecutive days

def days(n,k,arr):
    ans=0
    maxans=0
    count=0
    left=0

    for right in range(n): 
        ans=right-left+1

        if arr[right]==0: 
            count+=1

        while count>k:

            if arr[left]==0:
                count-=1
            left+=1
                
        maxans=max(maxans,right-left+1)
        
    return maxans

print(days(6,0,[1,1,0,1,1,1]))