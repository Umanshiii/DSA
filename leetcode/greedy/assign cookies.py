greed=[1,5,3,3,4]
s=[4,2,1,2,1,3]
greed.sort() #nlogn
s.sort() #mlogn
left=0
right=0
while left<len(s): #n
    if greed[right]<=s[left]:
        right+=1
    left+=1
print(right)

#o(nlogn+mlogn+m)
#o(1)