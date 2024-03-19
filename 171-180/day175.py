import random
times = 0
results = [0,0,0]
while results[0] != 3012 or results[1] != 1656 or results[2] != 332:
    times += 1
    state = 'a'
    steps = 5000
    probabilities = [
        ['a','a',0.9],
        ['a','b',0.075],
        ['a','c',0.025],
        ['b','a',0.15],
        ['b','b',0.8],
        ['b','c',0.05],
        ['c','a',0.25],
        ['c','b',0.25],
        ['c','c',0.5],
    ]
    results = [0,0,0]
    for j in range(steps):
        if state == 'a':
            results[0] += 1
            r = random.random()
            a = 0
            for i in range(3):
                a += probabilities[i][2]
                if r < a:
                    state = probabilities[i][1]
                    break
        elif state == 'b':
            results[1] += 1
            r = random.random()
            a = 0
            for i in range(3):
                a += probabilities[i+3][2]
                if r < a:
                    state = probabilities[i+3][1]
                    break
        elif state == 'c':
            results[2] += 1
            r = random.random()
            a = 0
            for i in range(3):
                a += probabilities[i + 6][2]
                if r < a:
                    state = probabilities[i + 6][1]
                    break
    if times % 100 == 0:
        print(times)
print(times)