#Rotate Array by K Steps
'''
Given an integer array nums and a non-negative integer k, 
rotate the array to the right by k steps.
'''
def rotate(arr, k):
    n=len(arr)
    k=k%n
    def rev(start, end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    rev(0,n-1)
    rev(0,k-1)
    rev(k,n-1)

    return arr