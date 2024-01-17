def modifiedSplit(string, delimiters):
    arr = []
    arr2 = []
    a = ""
    a2 = ""
    aa = False
    for i in string:
        if not i in delimiters:
            if aa:
                arr2.append(a2)
                aa = False
                a2 = ""
            a += i
        else:
            if not aa:
                arr.append(a)
                aa = True
                a = ""
            a2 += i
    if a != "":
        arr.append(a)
    if a2 != "":
        arr2.append(a2)
    arr.reverse()
    return [arr,arr2]
string = "hello//world:here"
delimiters = ["/",":"]
m = modifiedSplit(string, delimiters)
i = 0
j = 0
final = ""
while i < len(m[0]) and j < len(m[1]):
    if i < len(m[0]):
        final += m[0][i]
        i += 1
    if j < len(m[1]):
        final += m[1][j]
        j += 1
if i < len(m[0]):
    final += m[0][i]
if j < len(m[1]):
    final += m[1][j]
print(final)
