'''
Given two strings, write a complete program from scratch to determine if they are anagrams of each other. 
Two strings are anagrams if they contain the exact same characters with the exact same frequencies, 
but the order of the characters can be different.
'''

def anagram(s1,s2):
    hashset={}
    if len(s1)!=len(s2):
        return False
    for i in s1:
        if i in hashset:
            hashset[i]+=1
        else:
            hashset[i]=1
    
    for j in s2:
        if j in hashset and hashset[j]>=1:
            hashset[j]-=1
        else:
            return False
            
    return True