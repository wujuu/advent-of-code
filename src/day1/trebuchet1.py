"""Part 1 of the https://adventofcode.com/2023/day/1"""

import re


def trebuchet1(input_: str) -> int:
    """Simply check for digits with regex and pick first and last on each line."""
    lines = input_.split("\n")
    acc = 0

    for line in lines:
        digits = [int(c) for c in line if re.compile(r"[0-9]").match(c)]
        acc += 10 * digits[0] + digits[-1]

    return acc
