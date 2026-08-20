'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
def isPalindrome(s: str) -> bool:
    string=''
    for a in s.lower():
        if a.isalnum():
            string+=a
    l=0
    r=len(string)-1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    else:
        return True
        


        
