def strToArr(string):
    a = []
    for i in string:
        a.append(i)
    return a

w = "ab"
s = "abxaba"
ww = strToArr(w)
ww.sort()
inds = []
for i in range(len(s)-len(w)+1):
    substr = s[i:i+len(w)]
    substr = strToArr(substr)
    substr.sort()
    if ww == substr:
        inds.append(i)
print(inds)
