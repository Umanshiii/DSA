#find frequency of all elements
def frequency(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    if i in freq:
        return freq[i]
    else:
        return -1
        
#find frequency of target element
for i in arr:
    if i==target:
        count+=1
return count