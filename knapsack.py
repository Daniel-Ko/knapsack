from collections import namedtuple as nt
from pprint import PrettyPrinter
import argparse
from random import randint
from itertools import product


def knapsack_test():
    Item = nt("Item", ["price", "weight", "n"])
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

def knapsack_01(knapsack_size: int, shop: tuple):
    Item = nt("Item", ["name", "price", "weight", "n"])
    Value = nt("Value", ["cost", "weight"])

    TOTAL_WEIGHT = knapsack_size

    #TODO: itertools.product for unknown num of nested loops 
    
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
print("r, s, p")
pp = PrettyPrinter()
print(pp.pprint(values))


def tester():
    
if __name__ == "__main__":
    tester()