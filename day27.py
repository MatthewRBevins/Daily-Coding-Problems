def check(strArr: list):
    while 1 == 1:
        found = 0
        for j in range(len(strArr)):
            if (j + 1) == len(strArr):
                break
            if strArr[j] == '(' and strArr[j + 1] == ')' or strArr[j] == '[' and strArr[j + 1] == ']' or strArr[j] == '{' and strArr[j + 1] == '}':
                del strArr[j]
                del strArr[j]
                found = 1
                break
        if found == 0:
            break

    if len(strArr) > 0:
        return False
    return True        
while 1 == 1:
    string = input("enter string: ")
    print(check(list(string)))
