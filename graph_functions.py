from collections import namedtuple as nt

Neighbour = nt("Neighbour", ["node", "edgeweight"])


class ComboNode:
    def __init__(self, combo, neighbors, val, weight):
        self.combo = ()
        self.neighbors: dict{} = {}
        self.val = 0
        self.weight = 0

    def edge(v2):
        if v2 not in neighbours:
            return False
        return neighbours[v2]

    def __hash__(self):
        return ''.join(str(i) for i in self.combo)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


def knapsack_ON_GT(knapsack_size: int, items: list):
    graph: dict{ComboNode: Neighbour} = {item: [] for item in items}
        
    for i in range(len(items)):
        curr_item = items[i]


def hasedge(graph, v1, v2):
    if v1 in graph:
        return v2 in graph[v1]
    return False


def neighbours(graph, v):
    if v in graph:
        return graph[v]
    return list()
