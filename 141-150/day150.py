import math
points = [[0,0],[5,4],[3,1]]
central = [1,2]
k = 2
def distance(pos1, pos2):
    return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)

distances = []
for i in points:
    distances.append([distance(central,i),i])
distances.sort()
finalReturn = []
for i in range(k):
    finalReturn.append(distances[i][1])
print(finalReturn)
