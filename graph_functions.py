from collections import namedtuple as nt

Neighbour = nt("Neighbour", ["node", "edgeweight"])


class ComboNode:
    def __init__(self, combo, val, weight):
        self.combo = combo
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


def knapsack_ON_GT(W, items):
    graph = []
    start_combo = tuple(0 for _ in items)

    start_node = ComboNode(
        combo=start_combo,
        val=value(start_combo, items),
        weight=weight(start_combo, items)
    )
    graph[start_node] = []

    create_graph(start_node, W, items, graph)

    for node in graph:
        print(f"{key.combo}: {[c.combo for c in key.neighbors]}")


def create_graph(prevnode: ComboNode, W: int, items: list, graph):

    # Generates n children of this combination
    for i in range(len(items)):

        child_combo = list(prevnode.combo)
        child_combo[i] += 1
        child_combo = tuple(child_combo)

        child_w = weight(child_combo, items)

        # base case is here
        if child_w > W:
            continue

        child_node = ComboNode(child_combo, weight=child_w,
                               val=value(child_combo, items))

        # if new node doesn't already exist
        if child_node not in graph:
            graph[child_node] = []

        # if new node isn't already a neighbor
        if child_node not in graph[prevnode]:
            graph[prevnode].append(child_node)

        create_graph(child_node, W, items, graph)


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
