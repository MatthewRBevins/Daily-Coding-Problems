d = ["cat", "calf", "dog", "bear"]
startLetters = []
for i in d:
    startLetters.append(i[0])
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
bests = []
for i in l:
    hasEven = False
    hasOdd = False
    for j in range(len(startLetters)):
        if i == startLetters[j]:
            if len(d[j]) % 2 == 0:
                hasEven = True
            else:
                hasOdd = True
    if hasEven and not hasOdd:
        bests.append(i)
print(bests)