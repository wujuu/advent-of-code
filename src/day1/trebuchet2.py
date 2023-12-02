"""Part 2 of the https://adventofcode.com/2023/day/1"""

import re


def trebuchet2(input_: str) -> int:
    """Solution based on lookahead regex to solve the problem with overlapping written digits."""

    digit_map = dict(
        one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9
    )
    naive_regex = "|".join(
        list(digit_map.keys()) + list(map(lambda x: str(x), digit_map.values()))
    )
    lookahead_regex = re.compile(rf"(?=({naive_regex}))")

    lines = input_.split("\n")
    acc = 0

    for line in lines:
        matches = list(lookahead_regex.findall(line))
        first = digit_map[matches[0]] if matches[0] in digit_map else int(matches[0])
        last = digit_map[matches[-1]] if matches[-1] in digit_map else int(matches[-1])

        acc += 10 * first + last

    return acc
