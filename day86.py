string = "(())"
g = 0
while "()" in string:
    toDel = []
    for i in range(len(string)-1):
        if string[i] == "(" and string[i+1] == ")":
            toDel.append(i)
            toDel.append(i+1)
            g += 2
    for i in toDel:
        newStr = ""
        for j in range(len(string)):
            if j != i:
                newStr += string[j]
        string = newStr
print(len(string)-g)