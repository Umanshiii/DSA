'''
Imagine you have a list of system logs or support tickets, 
and each one is labeled with a severity level: Low, Medium, or High. 
They are mixed up in an array, like this:

["Medium", "Low", "High", "Medium", "Low", "High", "Low"]
[0, 1, 2, 0, 1, 2]
[0, 0, 1, 1, 2, 2]
'''

def risk(arr):
    low=0
    high=len(arr)-1
    mid=0
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1        

    return arr

print(risk([2,1,2,1,2,0,1,0,1,0,2]))
