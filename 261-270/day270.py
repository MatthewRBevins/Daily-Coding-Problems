import heapq

from tensorflow.python.training.moving_averages import weighted_moving_average


def dijkstra(graph, start, toAppend):
    # Initialize distances as infinity except for the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    # Loop until all paths are the shortest possible
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # If current path is greater than known path, skip
        if current_distance > distances[current_node]:
            continue

        # Look through all neighbors to current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight + toAppend

            # If a shorter path is found, update queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

        return distances

graph = {
    '0': [('1', 5), ('2', 3), ('5', 4)],
    '1': [('3', 8)],
    '2': [('3', 1)],
    '3': [('5', 10), ('4', 5)],
    '4': [],
    '5': []
}
graphTimes = []
for i in graph:
    start = i
    toAdd = 0
    if len(graphTimes) == 6:
        toAdd = graphTimes[int(i)]
    shortest_paths = dijkstra(graph, start, toAdd)
    for j in shortest_paths:
        if len(graphTimes) == 6 and (graphTimes[int(j)] == float('inf') or shortest_paths[j] < graphTimes[int(j)]) and shortest_paths[j] != 0:
            graphTimes[int(j)] = shortest_paths[j]
        elif len(graphTimes) < 6:
            graphTimes.append(shortest_paths[j])
print(max(graphTimes))