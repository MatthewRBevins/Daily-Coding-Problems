flights = [('SFO','HKO'),('YYZ','SFO'),('YUL','YYZ'),('HKO','ORD')]
start = 'YUL'
def findIten(flights, start):
    iten = [start]
    while len(flights) > 0:
        for j,i in enumerate(flights):
            if i[0] == start:
                iten.append(i[1])
                start = i[1]
                del flights[j]
                break
            if j == len(flights)-1:
                return False
    return iten
print(findIten(flights, start))
