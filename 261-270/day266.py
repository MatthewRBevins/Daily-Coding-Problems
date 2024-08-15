def checkAnagram(word1, word2):
    word2 = list(word2)
    for i in word1:
        if i in word2:
            del word2[word2.index(i)]
    return len(word2) == 0

word = "APPLE"
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dictionary = ["APPEAL"]
stepWords = []
for i in dictionary:
    for j in letters:
        if checkAnagram(word + j, i):
            stepWords.append(i)
            break
print(stepWords)