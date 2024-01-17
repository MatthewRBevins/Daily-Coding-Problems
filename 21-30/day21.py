def calcRooms(lectures):
    rooms = []
    for lecture in lectures:
        canFit = False
        for room in rooms:
            if lecture[1] < room[0] or lecture[0] > room[1]:
                canFit = True
                break
        if not canFit:
            rooms.append(lecture)
    return len(rooms)

lectures = [[30,75],[0,50],[60,150]]
print(calcRooms(lectures))
