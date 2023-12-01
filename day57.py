string = "the quick brown fox jumps over the lazy dog"
k = 10
lines = []
cLine = ""
for i in string.split(" "):
    if len(cLine) > 0 and len(cLine + " " + i) <= 10:
        cLine += " " + i
    elif len(cLine + i) <= 10:
        cLine += i
    else:
        lines.append(cLine)
        cLine = i
lines.append(cLine)
print(lines)
