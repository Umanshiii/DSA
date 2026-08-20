class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','{':'}','[':']'}
        st=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in d.keys():
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if d[top]!=i:
                    return False
        return True if len(st)==0 else False