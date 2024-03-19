mappings = []
mappedTo = []
s1 = "foo"
s2 = "bar"
for i in range(len(s1)):
    if s1[i] in mappings and s2[i] != mappedTo[mappings.index(s1[i])]:
        print("NO")
        break
    if not s1[i] in mappings:
        mappings.append(s1[i])
        mappedTo.append(s2[i])
