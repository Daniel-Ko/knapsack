from collections import namedtuple as nt
from queue import PriorityQueue

Neighbour = nt("Neighbour", ["node", "edgeweight"])


class ComboNode:
    def __init__(self, combo, val, weight):
        self.combo = combo
        self.val = val
        self.weight = weight

    def __hash__(self):
        return hash(self.combo)

    def __eq__(self, other):
        # return ''.join(str(i) for i in self.combo) == "".join(str(j) for j in other.combo)
        return self.__hash__() == other.__hash__()


def knapsack_0N_GT(W, items):
    graph = {}
    start_combo = tuple(0 for _ in items)

    start_node = ComboNode(
        combo=start_combo,
        val=value(start_combo, items),
        weight=weight(start_combo, items)
    )
    graph[start_node] = []

    create_graph(start_node, W, items, graph)

    # for node in graph:
    #     print(f"{node.combo}: {[c.combo for c in graph[node]]}")

    max_node = graph_backtrack(start_node, graph)

    return max_node


def create_graph(prevnode: ComboNode, W: int, items: list, graph):
    # Generates n children of this combination
    for i in range(len(items)):
        if prevnode.combo[i] >= items[i].n:
            continue

        child_combo = list(prevnode.combo)
        child_combo[i] += 1
        child_combo = tuple(child_combo)

        child_w = weight(child_combo, items)

        # base case is here
        if child_w > W:
            continue

        child_node = ComboNode(child_combo, weight=child_w,
                               val=value(child_combo, items))

        # if new node doesn't already exist, make new key and use it from here on
        if child_node not in graph:
            graph[child_node] = []

        # if new node isn't already a neighbor
        if child_node not in graph[prevnode]:
            graph[prevnode].append(child_node)

        create_graph(child_node, W, items, graph)


def graph_backtrack(start_node, graph):
    max_node = None
    max_val = 0
    for node in graph:
        # if empty, it is a 'leaf' and a solution
        if not graph[node]:
            if node.val > max_val:
                max_node = node
                max_val = node.val

    return max_node


def weight(combo, items):
    return sum(
        (item.weight * combo[i] for i, item in enumerate(items)))


def value(combo, items):
    return sum((item.value * combo[i]
                for i, item in enumerate(items)))
