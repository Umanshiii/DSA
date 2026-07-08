#Next greater element

def next(arr):
    result=[]
    for left in range(len(arr)):
        flag=False
        right=left+1
        while right<len(arr):    
            if arr[left]<arr[right]:
                result.append(arr[right])
                flag=True
                break
            else:
                right+=1
        if not flag:
            result.append(-1)

    return result

print(next([3,4,10,5,6,7]))