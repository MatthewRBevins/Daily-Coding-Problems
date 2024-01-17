# encoding
string = "AAAABBBCCDAA"
c = string[0]
n = 0
encoded = ""
for i in string:
    if i == c:
        n += 1
    else:
        encoded += (str(n) + c)
        c = i
        n = 1
encoded += (str(n) + c)
print(encoded)

decoded = ""
#decoding
for i in range(len(encoded)):
    if not encoded[i].isdigit():
        for j in range(int(encoded[i-1])):
            decoded += encoded[i]
print(decoded)
            
