from collections import defaultdict
from enum import Enum


class TraversalState(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def create_dic(self, dict_):
        g = Graph()
        for key, value in dict_.items():
            for element in value:
                self.graph[key].append(element)
        return g

    def add_edge(self, u, v):
        self.graph[u].append(v)


# represent the graph
example_graph_with_cycle = {'A': ['B', 'C'],
                            'B': ['D'],
                            'C': ['F'],
                            'D': ['E', 'F'],
                            'E': ['B'],
                            'F': []}

example_graph_without_cycle = {'A': ['B', 'C'],
                               'B': ['D', 'E'],
                               'C': ['F'],
                               'D': ['E'],
                               'E': [],
                               'F': []}


def is_in_cycle(graph, traversal_states, vertex):
    if traversal_states[vertex] == TraversalState.GRAY:
        return True
    traversal_states[vertex] = TraversalState.GRAY
    for neighbor in graph[vertex]:
        if is_in_cycle(graph, traversal_states, neighbor):
            return True
    traversal_states[vertex] = TraversalState.BLACK
    return False


def contains_cycle(graph):
    traversal_states = {vertex: TraversalState.WHITE for vertex in graph}
    for vertex, state in traversal_states.items():
        if (state == TraversalState.WHITE and
                is_in_cycle(graph, traversal_states, vertex)):
            return True
    return False


print(contains_cycle(example_graph_with_cycle))
print(contains_cycle(example_graph_without_cycle))
