'''move zeroes to the end'''

def move(arr):
    ind=[]
    count=0
    for i in range(len(arr)):
        if arr[i]!=0:
            ind.append(arr[i])
        else:
            count+=1

    for i in range(count):
        ind.append(0)

    return ind
