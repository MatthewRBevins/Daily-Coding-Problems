string = "acbbac"
for i in range(len(string)):
    if string[i] in string[0:i]:
        print(string[i])
        break