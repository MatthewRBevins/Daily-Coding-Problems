V = [5, 10, 10, 25, 5, 25, 50, 25, 5]
player1 = 0
player2 = 0

vv = V.copy()
gain1 = V[0] - max([V[1], V[len(V)-1]])
gain2 = V[len(V)-1] - max([V[0], V[len(V)-1]])
