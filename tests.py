from collections import namedtuple as nt
from random import randint
import time

from knapsack import knapsack_01_DF, knapsack_01_BF

Item = nt("Item", ["name", "value", "weight", "n"])


def gen_rand_test_cases(n):
    """ A rough test case generator """

    # Emerald was my favourite.
    item_names = (
        "Gold",
        "Silver",
        "Crystal",
        "Ruby",
        "Sapphire",
        "Emerald",
        "Diamond",
        "Pearl",
        "Platinum",
    )
    sack_size = randint(10, 30)
    num_items = randint(1, 10)

    item_weight_range = (
        sack_size // num_items,
        sack_size // 2 if sack_size // 2 > sack_size // num_items else sack_size,
    )

    shop = [
        Item(item_names[i], randint(1, 150), randint(*item_weight_range), n)
        for i in range(num_items)
    ]

    return (sack_size, shop)


def run_tests():
    test0_1DF_case1()
    test0_1DF_case2()

    test0_1BF_case1()
    test0_1BF_case2()


def test0_1DF_case1():
    actual_lookup = knapsack_01_DF(
        7,
        [
            Item("Ruby", 1, 1, 1),
            Item("Sapphire", 4, 3, 1),
            Item("Pearl", 5, 4, 1),
            Item("Diamond", 7, 5, 1),
        ],
    )
    expected_lookup = [
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 4, 5, 5, 5, 5],
        [0, 1, 1, 4, 5, 6, 6, 9],
        [0, 1, 1, 4, 5, 7, 8, 9],
    ]
    try:
        assert actual_lookup == expected_lookup
    except AssertionError as e:
        print("Test Case 1 for Knapsack 0-1 with DF failed")
        print(e)


def test0_1DF_case2():
    actual_lookup = knapsack_01_DF(23, [Item("Ruby", 71, 23, 1)])
    expected_lookup = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71]]
    try:
        assert actual_lookup == expected_lookup
    except AssertionError as e:
        print("Test Case 2 for Knapsack 0-1 with DF failed")
        print(e)


def test0_1BF_case1():
    actual_val, combo = knapsack_01_BF(
        7,
        [
            Item("Ruby", 1, 1, 1),
            Item("Sapphire", 4, 3, 1),
            Item("Pearl", 5, 4, 1),
            Item("Diamond", 7, 5, 1),
        ],
    )
    expected_val = 9
    try:
        assert actual_val == expected_val
    except AssertionError as e:
        print("Test Case 1 for Knapsack 0-1 with BF failed")
        print(e)


def test0_1BF_case2():
    actual_val, combo = knapsack_01_BF(23, [Item("Ruby", 71, 23, 1)])
    expected_val = 71

    try:
        assert actual_val == expected_val
    except AssertionError as e:
        print("Test Case 2 for Knapsack 0-1 with BF failed")
        print(e)


def test0_1_runtime(algo):
    times = []
    sack = [Item("Ruby", 1, 1, 1), Item("Sapphire", 4, 3, 1), Item(
        "Pearl", 5, 4, 1), Item("Diamond", 7, 5, 1)]
    # 4 x 5000 combinations
    start1 = time.time()
    algo(5000, sack)
    times.append(time.time() - start1)

    # 4 x 10000 combinations
    start2 = time.time()
    algo(10000, sack)
    times.append(time.time() - start2)

    # 4 x 20000 combinations
    start3 = time.time()
    algo(20000, sack)
    times.append(time.time() - start3)

    # 4 x 40000 combinations
    start4 = time.time()
    algo(40000, sack)
    times.append(time.time() - start4)

    # 4 x 250000 combinations
    start5 = time.time()
    algo(250000, sack)
    times.append(time.time() - start5)

    # 4 x 1000000 combinations
    start6 = time.time()
    algo(1000000, sack)
    times.append(time.time() - start6)

    print(times)
