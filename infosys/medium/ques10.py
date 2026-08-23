#Subarray sum equals k (prefix sum)

def subarray(arr, k):
    count = 0
    currsum = 0
    prefix_counts = {0: 1} 
    
    for num in arr:
        currsum += num
        if (currsum - k) in prefix_counts:
            count += prefix_counts[currsum - k]
            
        prefix_counts[currsum] = prefix_counts.get(currsum, 0) + 1
        
    return count