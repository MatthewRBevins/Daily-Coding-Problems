# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/072.py

from typing import Dict, List, Optional, Set, Tuple


class GraphPath:
    def __init__(
        self, nodes: Set[str] = set(), letter_counts: Dict[str, int] = dict()
    ) -> None:
        self.nodes = nodes
        self.letter_counts = letter_counts

    def __repr__(self) -> str:
        return "nodes={}, letters={}".format(self.nodes, self.letter_counts)


def get_max_value_string_helper(
    graph_path: GraphPath, node: str, adjacency_map: Dict[str, Set[str]]
) -> List[GraphPath]:
    if node in graph_path.nodes:
        return [graph_path]

    new_nodes = graph_path.nodes.copy()
    new_nodes.add(node)
    new_letter_counts = graph_path.letter_counts.copy()
    if node[0] not in new_letter_counts:
        new_letter_counts[node[0]] = 0
    new_letter_counts[node[0]] += 1

    new_graph_path = GraphPath(new_nodes, new_letter_counts)

    if node not in adjacency_map:
        return [new_graph_path]

    paths = list()
    for child_node in adjacency_map[node]:
        new_paths = get_max_value_string_helper(
            new_graph_path, child_node, adjacency_map
        )
        paths.extend(new_paths)
    return paths


def get_max_value_string(
    graph_string: str, edge_list: List[Tuple[int, int]]
) -> Optional[int]:
    letter_counts = dict()
    nodes = list()
    for char in graph_string:
        if char not in letter_counts:
            letter_counts[char] = 0
        else:
            letter_counts[char] += 1
        nodes.append("{}{}".format(char, letter_counts[char]))

    adjacency_map = dict()
    for start, end in edge_list:
        if nodes[start] not in adjacency_map:
            adjacency_map[nodes[start]] = set()
        if nodes[start] != nodes[end]:
            adjacency_map[nodes[start]].add(nodes[end])

    paths = list()
    graph_path = GraphPath()
    for node in adjacency_map:
        new_paths = get_max_value_string_helper(graph_path, node, adjacency_map)
        paths.extend(new_paths)

    max_value = 0
    for path in paths:
        max_path_value = max(path.letter_counts.values())
        if max_path_value > max_value:
            max_value = max_path_value
    return max_value if max_value > 0 else None


if __name__ == "__main__":
    print(get_max_value_string("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))
    print(get_max_value_string("A", [(0, 0)]))