from random import randint
words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string = 'bedbathandbeyond'
sentence = []
usedJ = []
for i in range(len(words)):
    randVal = randint(0,len(words)-1)
    for j in range(len(string)-len(words[randVal])+1):
        canUse = True
        for k in range(j,j+len(words[randVal])):
            if k in usedJ:
                canUse = False
        if canUse and string[j:j+len(words[randVal])] == words[randVal]:
            sentence.append([j, words[randVal]])
            for k in range(j,j+len(words[randVal])):
                usedJ.append(k)
            break
    del words[randVal]
print(sorted(sentence))
