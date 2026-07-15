#Top K Frequent Elements
'''
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
'''

def frequency(arr, k):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    data=dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    result=[]
    for i in data.keys():
        result.append(i)

    return result[:k]