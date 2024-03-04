string = "obb"
newString = ""
usedI = []
for i in range(len(string)):
    if not i in usedI:
        for j in range(i+1,len(string)):
            if not string[j] in usedI and string[j] == string[i]:
                usedI.append(i)
                usedI.append(j)
if len(usedI) == len(string)-1:
    print("YES")
else:
    print("NO")