from collections import namedtuple as nt
from random import randint

from knapsack import knapsack_01

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
    test0_1_case_one()
    test0_1_case_two()

def test0_1_case_one():
    actual_lookup = knapsack_01(
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
        print("Test Case 1 for K0-1 failed")
        print(e)


def test0_1_case_two():
    actual_lookup = knapsack_01(23, [Item("Ruby", 71, 23, 1)])
    expected_lookup = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71]]
    try:
        assert actual_lookup == expected_lookup
    except AssertionError as e:
        print("Test Case 2 for K0-1 failed")
        print(e)
