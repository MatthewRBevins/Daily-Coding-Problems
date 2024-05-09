V = [5, 10, 10, 25, 5, 25, 50, 25, 5]
player1 = 0
player2 = 0

vv = V.copy()
gain1 = V[0] - max([V[1], V[len(V)-1]])
gain2 = V[len(V)-1] - max([V[0], V[len(V)-1]])
# True = player 1, False = player 2
playing = True

while len(V) > 0:
    if len(V) == 1:
        if playing:
            player1 += V[0]
        else:
            player2 += V[0]
        break
    gain1 = V[0] - max([V[1], V[len(V) - 1]])
    gain2 = V[len(V) - 1] - max([V[0], V[len(V) - 1]])
    if playing:
        if gain1 > gain2:
            player1 += V[0]
            del V[0]
        elif gain2 > gain1:
            player1 += V[len(V)-1]
            del V[len(V)-1]
        playing = False
    else:
        if gain1 > gain2:
            player2 += V[0]
            del V[0]
        elif gain2 > gain1:
            player2 += V[len(V) - 1]
            del V[len(V) - 1]
        playing = True
print(player1)
print(player2)