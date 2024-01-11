bits = "10101010"
newBits = ""
for i in range(1,len(bits),2):
    newBits += bits[i]
    newBits += bits[i-1]
print(newBits)