"""Part 2 of the https://adventofcode.com/2023/day/4"""

import re
from functools import lru_cache


def extract_nums(winning_raw):
    return map(int, re.compile("[0-9]+").findall(winning_raw))


def scratchcards2(input_: str) -> int:
    """Solved using recursion with memoization"""
    cards = input_.split("\n")

    @lru_cache()
    def compute_points(idx: int) -> int:
        _, values = cards[idx].strip().split(":")
        winning_raw, actual_raw = values.split("|")
        winning, actual = extract_nums(winning_raw), extract_nums(actual_raw)

        matches = len(set(winning).intersection(set(actual)))
        return 1 + sum(compute_points(idx + offset + 1) for offset in range(matches))

    return sum(compute_points(i) for i in range(len(cards)))
