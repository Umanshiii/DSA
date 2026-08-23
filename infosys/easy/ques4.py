#Longest Substring Without Repeating Characters

def string(s):
    dic=set()
    left=0
    maxlen=0
    for right in range(len(s)):
        
        while s[right] in dic:
            dic.remove(s[left])
            left+=1

        dic.add(s[right])
        maxlen=max(maxlen,right-left+1)

    return maxlen


print(string(''))