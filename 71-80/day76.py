letters = [
    ['c','b','a'],
    ['d','a','f'],
    ['g','h','i']
]
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(letters[0])):
    prev = -1
    if i == len(letters[0]):
        break
    for j in range(len(letters)):
        cur = l.index(letters[j][i])
        if cur < prev:
            for k in range(len(letters)):
                del letters[k][i]
            i -= 1
            break
        prev = cur
print(letters)