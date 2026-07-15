#Longest Substring Without Repeating Characters
'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''
def demo(s):
    s1=set()
    size=0
    left,right=0,0
    while right < len(s):
        if s[right] not in s1:
            s1.add(s[right])
        else:
            while s[right] in s1:
                s1.remove(s[left])
                left+=1
            s1.add(s[right])

        size=max(right - left + 1,size)
        right+=1
        
    return size