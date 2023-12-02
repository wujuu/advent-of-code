"""Part 2 of the https://adventofcode.com/2023/day/2"""

import math
import re
from functools import reduce


COLORS = ["red", "blue", "green"]


def cubes2(input_: str) -> int:
    """Using regex and reduce insanity. Good look finding out what's going on here!"""
    colors_regex = re.compile("|".join(rf"[0-9]+ {color}" for color in COLORS))

    return sum(
        reduce(
            lambda x, y: x * y,
            reduce(
                lambda acc, x: {**acc, x[1]: max(acc[x[1]], int(x[0]))},
                [x.split() for x in colors_regex.findall(game)],
                {color: -math.inf for color in COLORS},
            ).values(),
        )
        for game in (input_.split("\n"))
    )
