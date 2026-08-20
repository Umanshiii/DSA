def palindrome(a,i,j):
    s=0
    f=0
    if a[i]==a[j] and i<j:
        f=1
        s+=a[j]+a[i]
        palindrome(a,i=i+1,j=j-1)
    elif a[i]==a[j] and i<j:
        f=0
        s+=a[j]+a[i]
        palindrome(a,i=i+1,j=j-1)
    elif i==j:
        s+=a[j]
    if f==1:
        return a,s,True
    else:
        return a,s,False

a=1221
i=0
j=len(str(a))-1     