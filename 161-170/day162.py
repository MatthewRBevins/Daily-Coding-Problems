list = ["dog", "cat", "apple", "apricot", "fish"]
prefs = []
for i in range(len(list)):
    prefix = ""
    for k in list[i]:
        prefix += k
        hasIt = False
        for j in range(len(list)):
            if j != i:
                if list[j][0:len(prefix)] == prefix:
                    hasIt = True
                    break
        if not hasIt:
            prefs.append(prefix)
            break
print(prefs)