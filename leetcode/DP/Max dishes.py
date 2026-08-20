A = [1,2,2,1,2,2,1,1,1,3,3,3,3,3,3,3,3,3,3,3]
N=len(A)
maxcount=0
dic={}
for i in range(N):
    if A[i] not in dic:
        dic[A[i]]=[i,]
    else:
        dic[A[i]].append(i)
for key,val in dic.items():
    count=1
    for i in range(1,len(val)):
        if A[i]-1!=A[i-1]:
            count+=1
    if count > maxcount:
        maxcount = count
        res = key
print(res)