'''
Oh!! Mankind is in trouble again. This time, it's a deadly disease spreading at a rate never seen before. The need of the hour is to set up efficient virus detectors. You are the lead at Central Hospital and you need to find a fast and reliable way to detect the footprints of the virus DNA in that of the patient.

The DNA of the patient as well as of the virus consists of lowercase letters. Since the collected data is raw, there may be some errors. You will need to find all substrings in the patient DNA that either exactly match the virus DNA or have at most one mismatch, i.e., a difference in at most one location.

For example, "aa" and "aa" are matching, "ab" and "aa" are matching, while "abb" and "bab" are not.
'''
def virusIndices(p, v):
    n, m = len(p), len(v)

    s = v + "#" + p
    z1 = [0]*len(s)
    l = r = 0
    for i in range(1, len(s)):
        if i <= r:
            z1[i] = min(r-i+1, z1[i-l])
        while i+z1[i] < len(s) and s[z1[i]] == s[i+z1[i]]:
            z1[i] += 1
        if i+z1[i]-1 > r:
            l, r = i, i+z1[i]-1

    s = v[::-1] + "#" + p[::-1]
    z2 = [0]*len(s)
    l = r = 0
    for i in range(1, len(s)):
        if i <= r:
            z2[i] = min(r-i+1, z2[i-l])
        while i+z2[i] < len(s) and s[z2[i]] == s[i+z2[i]]:
            z2[i] += 1
        if i+z2[i]-1 > r:
            l, r = i, i+z2[i]-1

    res = []
    for i in range(n-m+1):
        left = z1[m+1+i]
        right = z2[m+1+(n-i-m)]
        if left + right >= m-1:
            res.append(i)

    if res:
        print(*res)
    else:
        print("No Match!")