'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        mapp = {}
        
        for i in range(len(pattern)):
            if pattern[i] in mapp:
                if mapp[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in mapp.values():
                    return False
                mapp[pattern[i]] = words[i]
        
        return True

