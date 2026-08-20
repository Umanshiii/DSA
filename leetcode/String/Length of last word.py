'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
def lengthOfLastWord(self, s: str) -> int:
    i=len(s)-1
    count=0
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1    
    return count
            

