# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/234.py

from typing import Set
from typing import Union

class GraphUndirectedWeighted:
    """
    Graph Undirected Weighted Class

    Functions:
    add_node: function to add a node in the graph
    add_edge: function to add an edge between 2 nodes in the graph
    """

    def __init__(self) -> None:
        self.connections = {}
        self.nodes = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: Union[int, str]) -> None:
        # Add a node in the graph if it is not in the graph
        if node not in self.connections:
            self.connections[node] = {}
            self.nodes += 1

    def add_edge(
        self, node1: Union[int, str], node2: Union[int, str], weight: int
    ) -> None:
        # Add an edge between 2 nodes in the graph
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
        self.connections[node2][node1] = weight


def get_maximum_spanning_tree_helper(
    graph: GraphUndirectedWeighted,
    curr_node: int,
    remaining_nodes: Set[int],
    weight: int,
) -> int:
    if not remaining_nodes:
        return weight

    scores = []
    for destination in graph.connections[curr_node]:
        if destination in remaining_nodes:
            rem_cp = set(remaining_nodes)
            rem_cp.remove(destination)
            new_score = get_maximum_spanning_tree_helper(
                graph,
                destination,
                rem_cp,
                weight + graph.connections[curr_node][destination],
            )
            scores.append(new_score)
    return max(scores)


def get_maximum_spanning_tree(graph: GraphUndirectedWeighted) -> int:
    node_set = set(graph.connections.keys())
    start_node = node_set.pop()

    weight = get_maximum_spanning_tree_helper(graph, start_node, node_set, 0)
    return weight


if __name__ == "__main__":
    graph = GraphUndirectedWeighted()

    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 2)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 4, 3)
    graph.add_edge(2, 4, 4)

    print(graph)
    print(get_maximum_spanning_tree(graph))

    graph = GraphUndirectedWeighted()

    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(3, 2, 3)
