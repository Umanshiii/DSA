'''
Write a complete program from scratch that reads a string and compresses it by replacing 
consecutive repeating characters with the character followed by the count of its repetitions. 
If a character appears only once, do not append the count 1.
'''
def ques(string):
    res=''
    count=0
    string+='#'
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count+=1
        else:
            count+=1
            if count>1:
                res=res+string[i]+str(count)
            else:
                res=res+string[i]
            count=0

    return res

print(ques('aabbboosee'))