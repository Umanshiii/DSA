'''
There are N friends seated in a row, numbered 1 to N.
A single-digit number is passed from the first friend down the line to the last friend. 
Each person tries to communicate the digit to the next person using non-verbal actions.  
The first digit (arr[0]) is the ground truth. 
Anyone who understands the enactment correctly will have the exact same digit as the first person. 
Anyone whose digit doesn't match the very first person's digit made a mistake.  
Find out how many friends did not understand or enact the digit correctly
'''

def new(arr, n):
    left=0
    count=0
    for right in range(n-1,0,-1):
        if arr[right]!=arr[left]:
            count+=1

    return count
