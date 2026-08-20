'''
Given a string s, find the length of the longest substring without duplicate characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
'''
def lengthOfLongestSubstring(self, s: str) -> int:
    r = 0
    l = 0
    lis = []
    length = 0        
    while r < len(s):
        while s[r] in lis:
            lis.remove(s[l])
            l += 1
        lis.append(s[r])
        length = max(length, len(lis))
        r += 1
    return length
