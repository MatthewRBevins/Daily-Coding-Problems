words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
lines = [""]
index = 0
for i in words:
    if len(lines[index]) + len((i)) <= k:
        lines[index] += (i + " ")
    else:
        lines[index] = lines[index][0:len(lines[index])-1]
        while len(lines[index]) < 16:
            toAdd = 0
            for j in range(len(lines[index])):
                jj = j + toAdd
                if lines[index][jj] == " ":
                    lines[index] = lines[index][0:jj] + " " + lines[index][jj:len(lines[index])]
                    toAdd += 1
                if len(lines[index]) >= 16:
                    break
        lines.append("")
        index += 1
        lines[index] += (i + " ")
lines[index] = lines[index][0:len(lines[index])-1]
while len(lines[index]) < 16:
    print("***")
    add = 0
    for k in range(len(lines[index])):
        k += add
        add = 0
        if lines[index][k] == " ":
            lines[index] = lines[index][0:k] + " " + lines[index][k:len(lines[index])]
            print(lines[index])
            add = 1
        if len(lines[index]) >= 16:
            break
print(lines)
