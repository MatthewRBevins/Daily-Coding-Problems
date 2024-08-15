linesOfCode = [10, 40, 200, 1000, 60, 30]
payment = [1, 1, 1, 1, 1, 1]
for index,val in enumerate(linesOfCode):
    if index > 0 and linesOfCode[index-1] < val:
        while payment[index] <= payment[index-1]:
            payment[index] += 1
    if index < len(linesOfCode)-1 and linesOfCode[index+1] < val:
        while payment[index] <= payment[index+1]:
            payment[index] += 1
print(payment)