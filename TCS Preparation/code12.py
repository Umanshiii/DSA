#Next greater element

def next(arr):
    result=[]
    for left in range(len(arr)):
        right=left+1
        while right<len(arr)-1:    
            if arr[left]<arr[right]:
                result.append(arr[right])
                break
            else:
                right+=1
        
    result.append(-1)
    return result

print(next([3,4,10,5,6,7]))