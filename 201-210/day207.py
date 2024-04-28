# value, then every node it's connected to
# bartite
b = [[69, 1, 2], [4, 0, 2], [5, 0, 1], [99, 4], [80, 3]]
# non-bartite
n = [[99, 1], [80, 0]]

def check_b(graph):
    g = [[0]]
    index = 0
    for i in range(len(graph)):
        for j in range(1,len(graph[i])):
            if graph[i][j] in g[index] or i == 0 or i in g[index]:
                pass
            else:
                g.append([3])
                index += 1
            g[index].append(graph[i][j])
    return len(g) == 2
print(check_b(b))
print(check_b(n))