'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        for i in magazine:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in ransomNote:
            if i not in freq or freq[i] == 0:
                return False
            else:
                freq[i]-=1
        return True   
