from collections import namedtuple as nt
import argparse
from random import randint
from itertools import product

import tests
import graph_functions


def knapsack_01_DP(knapsack_size: int, items: list):
    """
        Params:
            items (3-tuple-> str, int, int, int): (name, weight, value, n)
    """
    # Add 1 more because array is 0-based, and we need a zero column
    total_size = knapsack_size + 1

    # Construct array of size [# of items][knapsack_weight]
    lookup = [[None for j in range(total_size)] for i in range(len(items))]

    # Fill in our top and left "boundaries" to provide a lookback for the algo:

    #   0th column
    for i, _ in enumerate(items):
        lookup[i][0] = 0

    #   1st item row.
    #   Easy -- fill with 0 if 1st item weight is under w, otherwise, we just use 1st item's value
    for w in range(total_size):
        lookup[0][w] = items[0].value if items[0].weight <= w else 0

    # Now construct lookup row by row, starting at the [1][1] spot and using our prefilled borders
    for i in range(1, len(items)):
        for w in range(1, total_size):
            curr_item = items[i]

            # Our item is too heavy to add to this subweight, use a prefilled value
            if curr_item.weight > w:
                lookup[i][w] = lookup[i - 1][w]
            else:
                # Keep the more valuable of what was in the sack before we added this item, or after we added it.
                lookup[i][w] = max(
                    lookup[i - 1][w],
                    lookup[i - 1][w - items[i].weight] + items[i].value,
                )
    return lookup


def knapsack_01_BF(knapsack_size: int, items: list):
    # Have n number of ranges from 0-1
    n_ranges = [range(1+1)] * len(items)

    # Then use itertools.product to make a full cartesian combination table. Technically O(n^2)
    combinations: tuple(tuple) = (product(*n_ranges))

    # Keep track of the maximum value throughout our n x n table
    max_value = 0
    max_combo = ()

    # The only thing left to do is evaluate whether this particular combination is the best
    for combo in combinations:

        combo_val = sum((item.value * combo[i]
                         for i, item in enumerate(items)))
        combo_weight = sum(
            (item.weight * combo[i] for i, item in enumerate(items)))

        if max_value < combo_val and combo_weight <= knapsack_size:
            max_value = combo_val
            max_combo = combo

    return (max_value, max_combo)


def knapsack_0N_DP(knapsack_size: int, items: list):
    """
        Params:
            items (3-tuple-> str, int, int, int): (name, weight, value, n)
    """
    # Add 1 more because array is 0-based, and we need a zero column
    total_size = knapsack_size + 1

    # Construct array of size [# of items][knapsack_weight]
    lookup = [[None for j in range(total_size)] for i in range(len(items))]

    # Prepopulate table with item value
    for i, item in enumerate(items):
        lookup[i][0] = 0
        for w in range(total_size):
            if w == 0:
                lookup[i][w] = 0
            else:
                lookup[i][w] = item.value * min((w // item.weight), item.n)

    # Now construct lookup row by row, starting at the [1][1] spot and using our prefilled borders
    for i in range(1, len(items)):
        for w in range(1, total_size):
            curr_item = items[i]

            # Our item is too heavy to add to this subweight, use a prefilled value
            if curr_item.weight > w:
                lookup[i][w] = lookup[i - 1][w]
            else:
                # Keep the more valuable of what was in the sack before we added this item, or after we added it.
                lookup[i][w] = max(
                    lookup[i - 1][w],
                    lookup[i - 1][w - items[i].weight] + items[i].value,
                    lookup[i][w]
                )
    return lookup


def knapsack_0n_GT(knapsack_size: int, items: list):
    ...


def print_dp(lookup, shop):
    """ Haha, a dirty printing method. Just use it. It should work. """
    print(f"Max Value: ${lookup[-1][-1]^3}", end="")
    print(" " * 11, end="")
    for w in range(len(lookup[0])):
        print(f"{w:>3}", end=" ")
    print()
    for row, item in zip(lookup, shop):
        print(
            f"{item.name:8} (${item.value:<2},{item.weight:^3}g, n={item.n:<2})", end="")
        for cell in row:
            print(f"{cell:3}", end=" ")
        print()


def print_bf(val, combo, shop):
    print(f"Max Value: ${val^3}", end="")
    print(" " * 6, end="")

    print(f"Exists", end=" ")
    print()
    for j, item in enumerate(shop):
        print(f"{item.name:8} (${item.value:<3},{item.weight:>3}g)", end="")
        print(f"{combo[j]:^8}", end=" ")
        print()


if __name__ == "__main__":
    Item = nt("Item", ["name", "value", "weight", "n"])

    tests.run_tests()

    parser = argparse.ArgumentParser(
        description="""
        1: run knapsack0-1 DP randomgen
        2: run knapsack0-1 BF randomgen
        3: run knapsack0-n DP randomgen
        4: run knapsack0-n GT randomgen
        """)
    parser.add_argument("-t", "--trial", type=int, default=0)
    args = parser.parse_args()

    if args.trial == 1:
        sack_size, shop = tests.test_case_gen(n=1)
        print_dp(knapsack_01_DP(sack_size, shop), shop)
    elif args.trial == 2:
        sack_size, shop = tests.test_case_gen(n=1)
        print_bf(*knapsack_01_BF(sack_size, shop), shop)
    elif args.trial == 3:
        sack_size, shop = tests.test_case_gen(n=10)
        print_dp(knapsack_0N_DP(sack_size, shop), shop)
    elif args.trial == 4:
        sack_size, shop = tests.test_case_gen(n=10)
        max_node = graph_functions.knapsack_0N_GT(sack_size, shop)
        print(f'{max_node.combo}: ${max_node.val}, {max_node.weight}g')

    # sack_size, shop = tests.test_case_gen(n=10)

    # lookup = knapsack_01_DP(sack_size, shop)
    # print_dp(lookup, shop)

    # tests.testDP_runtime(knapsack_0N_DP)
    # graph_functions.knapsack_0N_GT(100, [
    #     Item("Ruby", 90, 9, 8),
    #     Item("Sapphire", 60, 6, 10),
    #     Item("Pearl", 145, 14, 5)
    # ])
