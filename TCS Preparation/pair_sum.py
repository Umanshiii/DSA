'''
Given an array of distinct integers and a target sum, write a complete program from scratch 
to find all unique pairs of elements in the array whose sum is equal to the target sum.
'''

def find_pair(arr, target):
    result=[]
    lis=set()
    for i in arr:
        com=target-i
        if com in lis:
            result.append((com,i))
        lis.add(i)

    return result

arr = list(map(int, input().split()))
target = int(input())

print(find_pair(arr,target))