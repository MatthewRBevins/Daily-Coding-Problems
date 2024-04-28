# value, [directedTo], [directedAt]
graph = [["A", ["B"], []], ["B", ["C"], ["A"]], ["C", [], ["B"]]]
for i in range(len(graph)):
    temp = graph[i][2]
    graph[i][2] = graph[i][1]
    graph[i][1] = temp
print(graph)