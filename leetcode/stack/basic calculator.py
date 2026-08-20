class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign=+1
        num=0
        numbers="0123456789"
        stack=[]

        for i in s:
            if i == ' ':
                continue
            if i.isdigit():
                num=num*10+int(i)
            elif i=='+' or i=='-':
                result+=sign*num
                num=0
                if i=='-':
                    sign=-1
                else:
                    sign=+1
            elif i=='(':
                stack.append(result)
                stack.append(sign)
                result=0
                sign=+1
            elif i==')':
                result += sign * num
                num=0
                result*=stack.pop()
                result+=stack.pop()
            
        result += sign * num
        return result