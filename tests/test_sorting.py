import pytest

import algorithms.sorting as sorting


def test_bubble_sort():
    tests = [
        {"to_sort": [4, 2, 1, 4, 5, 10, 3], "expected": [1, 2, 3, 4, 4, 5, 10]},
        {"to_sort": [1, 2, 3, 4, 4, 5, 10], "expected": [1, 2, 3, 4, 4, 5, 10]},
        {"to_sort": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5]},
    ]

    for test in tests:
        result = sorting.bubble_sort(test["to_sort"])
        assert result == test["expected"]


def test_swap():
    tests = [
        {"to_swap": [1, 2, 3], "first": 0, "second": 2, "expected": [3, 2, 1]},
        {"to_swap": [1, 2, 3], "first": 0, "second": 0, "expected": [1, 2, 3]},
    ]

    for test in tests:
        sorting.swap(test["to_swap"], test["first"], test["second"])
        result = test["to_swap"]
        assert result == test["expected"]


def test_swap_invalid():
    tests = [{"to_swap": [1, 2, 3], "first": 0, "second": 3}]

    for test in tests:
        with pytest.raises(Exception) as e_info:
            sorting.swap(test["to_swap"], test["first"], test["second"])
