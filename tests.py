from collections import namedtuple as nt
from random import randint
import time
from itertools import cycle
from statistics import mean

from knapsack import knapsack_01_DP, knapsack_01_BF

Item = nt("Item", ["name", "value", "weight", "n"])


def test_case_gen(num_items=9, w=-1, n=-1):
    """ A rough test case generator """

    # Emerald was my favourite.
    item_names = cycle((
        "Gold",
        "Silver",
        "Crystal",
        "Ruby",
        "Sapphire",
        "Emerald",
        "Diamond",
        "Pearl",
        "Platinum",
    ))
    sack_size = w if w > -1 else randint(10, 30)
    num_items = randint(1, num_items)
    item_weight_range = (
        sack_size // num_items,
        sack_size // 2 if sack_size // 2 > sack_size // num_items else sack_size,
    )

    shop = [
        Item(next(item_names), randint(1, 50), randint(*item_weight_range), randint(1, n)) for i in range(num_items)
    ]

    return (sack_size, shop)


def run_tests():
    test0_1DF_case1()
    test0_1DF_case2()

    test0_1BF_case1()
    test0_1BF_case2()


def test0_1DF_case1():
    actual_lookup = knapsack_01_DP(
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
    actual_lookup = knapsack_01_DP(23, [Item("Ruby", 71, 23, 1)])
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


def testDP_runtime(algo, n=1):
    times = []

    # 500 x 4 combinations
    times.append(timetest(algo, test_case_gen(num_items=500, w=4, n=n)))

    # 50 x 40 combinations
    times.append(timetest(algo, test_case_gen(num_items=5000, w=8, n=n)))

    # 500 x 16 combinations
    times.append(timetest(algo, test_case_gen(num_items=500, w=16, n=n)))

    # 500 x 32 combinations
    times.append(timetest(algo, test_case_gen(num_items=500, w=32, n=n)))

    # 5000 x 32 combinations
    times.append(timetest(algo, test_case_gen(num_items=5000, w=32, n=n)))

    # 50000 x 100 combinations
    times.append(timetest(algo, test_case_gen(num_items=50000, w=100, n=n)))

    # 50000 x 200 combinations
    times.append(timetest(algo, test_case_gen(num_items=50000, w=200, n=n)))

    print(times)


def testBF_runtime(algo):
    """ Need small num_item values because brute force is O(2^n)! w does not matter """
    times = []

    # 2^10 combinations
    times.append(timetest(algo, test_case_gen(num_items=10, w=10, n=1)))

    # 2^15
    times.append(timetest(algo, test_case_gen(num_items=15, w=10, n=1)))

    # 2^20
    times.append(timetest(algo, test_case_gen(num_items=20, w=10, n=1)))

    # 2^25
    times.append(timetest(algo, test_case_gen(num_items=25, w=32, n=1)))

    # 2^27
    times.append(timetest(algo, test_case_gen(num_items=27, w=32, n=1)))

    # 2^30
    times.append(timetest(algo, test_case_gen(num_items=30, w=100, n=1)))

    # 2^32 yikes
    times.append(timetest(algo, test_case_gen(num_items=32, w=200, n=1)))

    print(times)


def timetest(algo, test_case):
    times = []
    for i in range(3):
        start = time.time()
        algo(*test_case)
        times.append(time.time() - start)
    return mean(times)
