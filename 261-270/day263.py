characterStream = ["H", "e", "l", "l", "o", " ", "m", "y", " ", "n", "a", "m", "e", " ", "i", "s", " ", "m", "a", "t", "t", "h", "e", "w", "."]
def isSentence(stream):
    sentenceStart = True
    sentenceNext = False
    prevSpace = False
    prevChar = ""
    for i in stream:
        if sentenceStart:
            sentenceStart = False
            sentenceNext = True
            if i == i.lower():
                return False
        elif sentenceNext:
            sentenceNext = False
            if i != i.lower() and i != " ":
                return False
        else:
            if i != i.lower():
                return False
        if i == " ":
            if prevSpace:
                return False
            prevSpace = True
        else:
            prevSpace = False
        if i in [".", "?", "!"]:
            sentenceStart = True
            if prevChar in [" ", ",", ";", ":", ".", "?", "!"]:
                return False
        prevChar = i
    return True
print(isSentence(characterStream))