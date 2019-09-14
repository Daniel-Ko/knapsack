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


def knapsack_01(knapsack_size: int, items: list):
    """
        Params:
            items (3-tuple-> str, int, int, int): (name, weight, value, n)
    """
    # Add 1 more because array is 0-based, and we need a zero column
    total_size = knapsack_size + 1

    # Construct array of size [# of items][knapsack_weight]
    lookup = [[None for j in range(total_size)] for i in range(len(items))]

    # Fill in our top and left "boundaries" to provide a lookback for the algo:

    #   the 0 column
    for i, _ in enumerate(items):
        lookup[i][0] = 0

    #   the 1st item row.
    #   Easy -- 0 if 1st item weight is under w, otherwise, we just use the value (used once)
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




def print_repr(lookup, shop):
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



if __name__ == "__main__":
    Item = nt("Item", ["name", "value", "weight", "n"])

    tests.run_tests()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="run knapsack0-1 DP randomgen")
    parser.add_argument("-b", help="run knapsack0-1 BF randomgen")
    parser.add_argument("-c", help="run knapsack0-n DP randomgen")
    parser.add_argument("-d", help="run knapsack0-n GT randomgen")

    args = parser.parse_args()

    n = 1

    sack_size, shop = tests.gen_rand_test_cases(1)

    lookup = knapsack_01(sack_size, shop)
    print_repr(lookup, shop)
