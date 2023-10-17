board = [[False,False,False,False],[True,True,False,True],[False,False,False,False],[False,False,False,False]]
start = [3,0]
end = [0,0]
while start != end:
    if start[0] > end[0] :
        start[0] -= 1
    elif start[0] < end[0]:
        start[0] += 1
