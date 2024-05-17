s = "aaabbc"
newS = ""
while True:
    for i in range(len(s)):
        if i >= len(s):
            break
        if len(newS) == 0 or newS[len(newS)-1] != s[i]:
            newS += s[i]
            s = s[:i] + s[i+1:]
    if len(s) == 0:
        break