str1 = "abcde"
str2 = "cdeab"
def shift(string):
    return string[1:] + string[0]
for i in range(len(str1)):
    str1 = shift(str1)
    if str1 == str2:
        print("YES")
