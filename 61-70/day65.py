matrix = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20]]
horizLim = [-1,len(matrix[0])]
vertLim = [0,len(matrix)]
horizDir = True
vertDir = True
horiz = 0
vert = 0
numbersPrinted = 0
while True:
    if numbersPrinted >= len(matrix)*len(matrix[0]):
        break
    for i in range(horizLim[0]+1, horizLim[1]):
        numbersPrinted+=1
        print(matrix[vert][i])
        horiz = i
    horizLim[1]-=1
    for i in range(vertLim[0]+1, vertLim[1]):
        numbersPrinted+=1
        print(matrix[i][horiz])
        vert = i
    vertLim[1]-=1
    for i in range(horizLim[1]-1, horizLim[0], -1):
        numbersPrinted+=1
        print(matrix[vert][i])
        horiz = i
    horizLim[0]+=1
    for i in range(vertLim[1]-1, vertLim[0], -1):
        numbersPrinted+=1
        print(matrix[i][horiz])
        vert = i
    vertLim[0]+=1
