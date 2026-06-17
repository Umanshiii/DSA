'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''
def rotate(self, nums, k):
    k = k % len(nums)   
    nums[:] = nums[-k:] + nums[:-k]
    return nums

class Solution:
    def rotateArr(self, arr, d):
        #code here
        n=len(arr)
        d=d%n
        start=0
        end=d-1
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
        
        start=d
        end=len(arr)-1
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
            
        start=0
        end=len(arr)-1
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
        
        return arr