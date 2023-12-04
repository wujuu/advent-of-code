"""Part 1 of the https://adventofcode.com/2023/day/4"""

import re


def scratchcards1(input_: str) -> int:
    """Straightforward iterative solution."""
    cards = input_.split("\n")
    acc = 0

    for card in cards:
        _, values = card.strip().split(":")
        winning_raw, actual_raw = values.split("|")

        winning = map(int, re.compile("[0-9]+").findall(winning_raw))
        actual = map(int, re.compile("[0-9]+").findall(actual_raw))

        matches = len(set(winning).intersection(set(actual)))
        points = 2 ** (matches - 1) if matches > 0 else 0
        acc += points

    return acc
