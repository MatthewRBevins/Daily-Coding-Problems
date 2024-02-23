word1 = "hello"
word2 = "world"
string = "dog cat hello cat dog dog hello cat world"
arr = string.split(" ")
bestDist = len(arr)
for i in range(len(arr)):
    if arr[i] == word1:
        # forwardDistance
        dist = 0
        for j in range(i+1,len(arr)):
            if arr[j] == word2:
                if dist < bestDist:
                    bestDist = dist
                    break
            dist += 1
        # backwardDistance
        dist = 0
        for j in range(i-1,0,-1):
            if arr[j] == word2:
                if dist < bestDist:
                    bestDist = dist
                    break
            dist += 1
print(bestDist)