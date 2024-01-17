# row = house in row, column = color, value = cost
costs = [[1, 5, 2], [2, 3, 1], [7, 3, 5], [6, 3, 2]]

def find_best_cost(cost, level, prevIndex):
    if level == len(costs):
        return cost
    bestCost = 1000
    for i in range(len(costs[level])):
        if i != prevIndex:
            currentCost = find_best_cost(cost+costs[level][i], level+1, i)
            if currentCost < bestCost:
                bestCost = currentCost
    return bestCost

print(find_best_cost(0, 0, -1))
    
