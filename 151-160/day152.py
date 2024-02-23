import random
numbers = [1,2,3,4]
probabilities = [0.1,0.5,0.2,0.2]
ranges = []
r = 0
for i in probabilities:
    r += i
    ranges.append(r)
for j in range(100):
    r = random.random()
    if r <= ranges[0]:
        print(numbers[0])
    else:
        for i in range(len(ranges)-1):
            if ranges[i] <= r <= ranges[i + 1]:
                print(numbers[i+1])
                break
