from collections import namedtuple as nt
from pprint import PrettyPrinter
import argparse
from random import randint
from itertools import product

Item = nt("Item", ["price", "weight", "n"])

def knapsack_test():
    Value = nt("Value", ["r", "s", "p", "cost", "weight"])

    TOTAL_WEIGHT = 100
    num_rubies = 1; num_sapphires = 1; num_pearls = 1

    rubies = Item(90, 9, num_rubies)
    sapphires = Item(60, 6, num_sapphires)
    pearls = Item(145, 14, num_pearls)

    values = []

    for i in range(num_rubies+1):
        for j in range(num_sapphires+1):
            for k in range(num_pearls+1):

                cost = i*rubies.price + j*sapphires.price + k*pearls.price
                weight = i*rubies.weight + j*sapphires.weight + k*pearls.weight

                print(f"{i}, {j}, {k} : cost={cost}, weight={weight}")

                # Might not all be the same weight!
                if weight > 100:
                    break

                values.append(Value(i, j, k, cost, weight))

def knapsack_01(knapsack_size: int, shop: dict):
    """
        Params:
            shop (dict:3-tuple-> int, int, int): (weight, value, n)
    """
    Item = nt("Item", ["name", "price", "weight", "n"])
    Value = nt("Value", ["cost", "weight"])

    TOTAL_WEIGHT = knapsack_size

    values = []

    n_sizes = (map(range, (item.n+1 for item in shop.values())))
    # print([a for a in product(range(4), range(2))])
    print(list(product(*n_sizes)))
    # for a in product(map(iter(range), n_sizes)):
    #     print(a)
    # for i in range(num_rubies+1):
    #     for j in range(num_sapphires+1):
    #         for k in range(num_pearls+1):

    #             cost = i*rubies.price + j*sapphires.price + k*pearls.price
    #             weight = i*rubies.weight + j*sapphires.weight + k*pearls.weight

    #             print(f"{i}, {j}, {k} : cost={cost}, weight={weight}")

    #             # Might not all be the same weight!
    #             if weight > 100:
    #                 break

    #             values.append(Value(i, j, k, cost, weight))
# print("r, s, p")
# pp = PrettyPrinter()
# print(pp.pprint(values))


if __name__ == "__main__":
    knapsack_01(100, {
        "Ruby": Item(90, 9, 1),
        "Sapphire": Item(60, 6, 1),
        "Pearl": Item(145, 14, 1)
    })