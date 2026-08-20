class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation=['+','-','*','/']
        lis=[]
        for i in tokens:
            if i in operation:
                a=lis.pop()
                b=lis.pop()

                if i == '+':
                    lis.append(b + a)
                elif i == '-':
                    lis.append(b - a)
                elif i == '*':
                    lis.append(b * a)
                else:
                    lis.append(int(b / a)) 
            else:
                lis.append(int(i))
            
        return lis[0]
                

        