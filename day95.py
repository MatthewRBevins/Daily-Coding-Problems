l = [1,3,2]
s = False
for i in range(len(l)-1,0,-1):
    sub = 0
    while i-sub > -1:
        if l[i-sub] < l[i]:
            t = l[i-sub]
            l[i-sub] = l[i]
            l[i] = t
            s = True
            break
        sub += 1
    if s:
        break
if not s:
    l.sort()
print(l)