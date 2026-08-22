#Rearrange string pieces

def string(s,n):
    def gcd(a,b):
        if a>b:
            large=a
        elif b>a:
            large=b
        else:
            return a

        ans=1
        for i in range(1, large+1):
            if a%i==0 and b%i==0:
                ans=i
                
        return ans

    dic={}
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    num=0
    for i,j in dic.items():
        num=gcd(num,j)

    return num