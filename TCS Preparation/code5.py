'''
Given a string from the input, write a complete program from scratch to count the total number of words in it. 
A word is defined as a sequence of characters separated by one or more spaces. 
Be careful: the input might have extra spaces at the beginning, at the end, or multiple spaces between words.
'''

#Example Input:  Welcome   to  TCS  NQT  
#Expected Output: 4

def count(string):
    lis=string.strip().split()
    total=len(lis)

    return total

string=input()
print(count(string))