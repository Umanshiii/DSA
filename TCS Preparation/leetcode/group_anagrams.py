#group anagrams
'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An anagram is a word formed by rearranging the letters of a 
different word, typically using all the original letters exactly 
once (e.g., "eat", "tea", and "ate" are all anagrams of each other).
'''
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

def anagram(strs):
    check={}
    result=[]
    for word in strs:
        new="".join(sorted(word))
        if key not in check:
            check[new]=[]
        check[new].append(word)
    for i in check.values():
        result.append(i)
    return result