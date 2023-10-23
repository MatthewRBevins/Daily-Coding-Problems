str1 = "kitten"
str2 = "sitting"
dis = abs(len(str1)-len(str2))
if str1 > str2:
    str1 = str1[0:len(str2)]
elif str1 < str2:
    str1 += str2[len(str1):len(str2)]
for i in range(len(str1)):
    if str1[i] != str2[i]:
        dis += 1
print(dis)
