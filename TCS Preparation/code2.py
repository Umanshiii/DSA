def rem(string):
    result=''
    vowel=['a','e','i','o','u']
    for i in string:
        if i.lower() not in vowel:
            result+=i
    return result if len(result)>0 else -1