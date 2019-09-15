from collections import namedtuple as nt
import argparse
from random import randint
from itertools import product

import tests

Item = nt("Item", ["price", "weight", "n"])


def naive_implementation():
    """ My own go before understanding how others have done it """
    Value = nt("Value", ["r", "s", "p", "cost", "weight"])

    TOTAL_WEIGHT = 100
    num_rubies = 1
    num_sapphires = 1
    num_pearls = 1

    rubies = Item(90, 9, num_rubies)
    sapphires = Item(60, 6, num_sapphires)
    pearls = Item(145, 14, num_pearls)

    values = []

    for i in range(num_rubies + 1):
        for j in range(num_sapphires + 1):
            for k in range(num_pearls + 1):

                cost = i * rubies.price + j * sapphires.price + k * pearls.price
                weight = i * rubies.weight + j * sapphires.weight + k * pearls.weight

                print(f"{i}, {j}, {k} : cost={cost}, weight={weight}")

                # Might not all be the same weight!
                if weight > 100:
                    break

                values.append(Value(i, j, k, cost, weight))


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


def knapsack_0n_DP(knapsack_size: int, items: list):
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
        for w in range(total_size):
            lookup[i][w] = items[i].value * (w // items[i].weight)

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


def knapsack0n_GT(knapsack_size: int, items: list):
    ...


def print_dp(lookup, shop):
    """ Haha, a dirty printing method. Just use it. It should work. """
    print(" " * 20, end="")
    for w in range(len(lookup[0])):
        print(f"{w:3}", end=" ")
    print()
    for row, item in zip(lookup, shop):
        print(f"{item.name:8} (${item.value:<3},{item.weight:>3}g)", end="")
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
    # tests.test0_1_runtime()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="run knapsack0-1 DP randomgen")
    parser.add_argument("-b", help="run knapsack0-1 BF randomgen")
    parser.add_argument("-c", help="run knapsack0-n DP randomgen")
    parser.add_argument("-d", help="run knapsack0-n GT randomgen")

    args = parser.parse_args()

    n = 1

    sack_size, shop = tests.test_case_gen(1)

    # lookup = knapsack_0n_DP(sack_size, shop)
    # print_dp(lookup, shop)

    tests.test0_1_runtime(knapsack_01_BF)
