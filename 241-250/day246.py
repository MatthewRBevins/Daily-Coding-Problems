import copy
words = ["chair", "height", "racket", "touch", "tunic"]
def findCircle(words, c):
    if len(c) == len(words):
        print(c)
        return True
    canAdd = False
    for i in range(len(words)):
        circle = copy.deepcopy(c)
        if not words[i] in circle and (len(circle) == 0 or words[i][0] == circle[len(circle)-1][-1]):
            canAdd = True
            circle.append(words[i])
            if findCircle(words, circle):
                return True
    if not canAdd:
        return False
print(findCircle(words, []))