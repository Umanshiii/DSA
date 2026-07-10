#Find the Longest Consecutive Subsequence
'''
Given an unsorted array of integers, write a complete program from scratch to find the length of the longest consecutive elements subsequence. 
The elements do not need to be contiguous in the original array, but they must form a continuous sequence of numbers (e.g., 1, 2, 3, 4).
'''

def longest_subsequence(arr):

    maxsub=0
    hashset=set(arr)

    for i in arr:

        if i-1 not in hashset:
            start=i
            subs=1

            while start+1 in hashset:
                subs+=1
                start+=1

            maxsub=max(subs, maxsub)
        
    return maxsub