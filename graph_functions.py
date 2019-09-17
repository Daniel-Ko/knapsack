from collections import namedtuple as nt

Neighbour = nt("Neighbour", ["node", "edgeweight"])


class ComboNode:
    def __init__(self, combo, val, weight):
        self.combo = ()
        self.neighbors = []
        self.val = val
        self.weight = weight

    def edge(v2):
        if v2 not in neighbours:
            return False
        return neighbours[v2]

    def __hash__(self):
        return hash(self.combo)

    def __eq__(self, other):
        # return ''.join(str(i) for i in self.combo) == "".join(str(j) for j in other.combo)
        return self.__hash__() == other.__hash__()


def graph_setup(W, items):
    graph = {}  # dict{ComboNode: Neighbour} = {item: [] for item in items}
    start_combo = tuple(1 for _ in items)

    start_node = ComboNode(
        combo=start_combo,
        val=value(start_combo, items),
        weight=weight(start_combo, items)
    )

    graph[start_node] = []

    knapsack_ON_GT(start_node, W, items, graph)


def knapsack_ON_GT(node: ComboNode, W: int, items: list, graph):

    for i in range(len(items)):
        curr_item = items[i]


def weight(combo, items):
    return sum(
        (item.weight * combo[i] for i, item in enumerate(items)))


def value(combo, items):
    return sum((item.value * combo[i]
                for i, item in enumerate(items)))


def hasedge(graph, v1, v2):
    if v1 in graph:
        return v2 in graph[v1]
    return False


def neighbours(graph, v):
    if v in graph:
        return graph[v]
    return list()
