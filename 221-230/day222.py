path = "/usr/bin/../bin/./scripts/../"
p = path.split("/")
c = []
for i in range(len(p)):
    if p[i] != "":
        if p[i] == ".":
            pass
        elif p[i] == "..":
            del c[len(c)-1]
        else:
            c.append(p[i])
print("/" + "/".join(c) + "/")