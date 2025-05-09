from collections import deque
from typing import List, Dict, Set


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.neighbors: List['Node'] = []

    def add_neighbor(self, neighbor: 'Node') -> None:
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.value})"


def connect_directed(a: Node, b: Node) -> None:
    a.add_neighbor(b)


def connect_undirected(a: Node, b: Node) -> None:
    a.add_neighbor(b)
    b.add_neighbor(a)


def build_graph(nodes_count: int, edges: List[tuple], directed: bool = True) -> Dict[int, Node]:
    nodes = {i: Node(i) for i in range(1, nodes_count + 1)}
    for src, dst in edges:
        if directed:
            connect_directed(nodes[src], nodes[dst])
        else:
            connect_undirected(nodes[src], nodes[dst])
    return nodes


def sum_of_neighbors(node: Node) -> int:
    return sum(n.value for n in node.neighbors)


def dfs(start: Node, visited: Set[Node] = None) -> None:
    if visited is None:
        visited = set()
    if start in visited:
        return
    print(start.value, end=' ')
    visited.add(start)
    for neighbor in start.neighbors:
        dfs(neighbor, visited)


def bfs(start: Node) -> None:
    visited: Set[Node] = set()
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        print(current.value, end=' ')
        visited.add(current)
        queue.extend(n for n in current.neighbors if n not in visited)


if __name__ == "__main__":
    directed_edges = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 1)]
    undirected_edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)]

    print("=== Направленный граф ===")
    g1 = build_graph(4, directed_edges, directed=True)
    print("Сумма соседей узла 1:", sum_of_neighbors(g1[1]))
    print("DFS: ", end='')
    dfs(g1[1])
    print("\nBFS: ", end='')
    bfs(g1[1])

    print("\n\n=== Ненаправленный граф ===")
    g2 = build_graph(4, undirected_edges, directed=False)
    print("Сумма соседей узла 2:", sum_of_neighbors(g2[2]))
    print("DFS: ", end='')
    dfs(g2[2])
    print("\nBFS: ", end='')
    bfs(g2[2])
