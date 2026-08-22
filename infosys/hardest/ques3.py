#Minimize Binary String Value

#ADJACENT SWAPS
def string(a,b,s,cash):
    output=''
    if a>=b:
        for i in s:
            if i=='1' and cash>=b:
                output+='0'
                cash-=b
            else:
                output+=i
        return output
    else:
        s=list(s)
        for i in range(len(s)):
            if s[i]=='1' and cash>=a:
                j=i+1
                while j<len(s) and s[j]!='0':
                    j+=1
                if j==len(s):
                    if b<=cash:
                        s[i]='0'
                        cash-=b
                        continue
                    else:
                        return ''.join(s)

                cost=(j-i)*a
                if cost<=cash and cost<=b:
                    s.pop(j)
                    s.insert(i,'0')
                    cash-=cost
                elif b<=cash and cost>b:
                    s[i]='0'
                    cash-=b
                elif cost>cash and b>cash:
                    return ''.join(s)
            elif cash>=b:
                s[i]='0'
                cash-=b
    return ''.join(s)

#DIRECT SWAP
def string(a,b,s,cash):
    output=''
    if a>=b:
        for i in s:
            if i=='1' and cash>=b:
                output+='0'
                cash-=b
            else:
                output+=i
        return output
    else:
        s=list(s)
        for i in range(len(s)):
            if s[i]=='1' and cash>=a:
                m=len(s)-1
                while m>i:
                    if s[m]=='0':
                        break
                    m-=1
                if m==i:
                    if cash>=b:
                        s[i]='0'
                        cash-=b
                else:
                    s[i],s[m]=s[m],s[i]
                    cash-=a                      
                
            elif cash>=b:
                s[i]='0'
                cash-=b
    return ''.join(s)