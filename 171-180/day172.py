s = "dogcatcatcodecatdog"
words = ["cat","dog"]
res = []
for i in range(len(s)):
    w = words.copy()
    length = len(w[0])
    for j in range(i,len(s),length):
        if s[j:j+length] in w:
            w.remove(s[j:j+length])
        else:
            break
        if len(w) == 0:
            res.append(i)
print(res)