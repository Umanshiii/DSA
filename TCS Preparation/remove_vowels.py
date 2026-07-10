'''
Given a string, remove all vowels (a, e, i, o, u) from it while preserving
the order of the remaining characters. Both uppercase and lowercase vowels
should be removed.
'''
def rem(string):
    result=''
    vowel=['a','e','i','o','u']
    for i in string:
        if i.lower() not in vowel:
            result+=i
    return result if len(result)>0 else -1