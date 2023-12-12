# each row represents a vertex, each column represents whether it's connected to that index
adjacency_matrix = [
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0]
]

def color(m, k):
    min_colors = 0
    for i in m:
        r = sum(i)+1
        min_colors = max(min_colors, r)
    return min_colors <= k
print(color(adjacency_matrix, 4))
