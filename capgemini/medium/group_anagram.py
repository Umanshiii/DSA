#https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for word in strs:
            temp=''.join(sorted(word))
            if temp in freq:
                freq[temp].append(word)
            else:
                freq[temp]=[word]
        lis=[]
        for key,val in freq.items():
            lis.append(val)

        return lis

