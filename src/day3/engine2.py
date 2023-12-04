"""Part 2 of the https://adventofcode.com/2023/day/3"""

import math


def is_number(char: str) -> bool:
    return char in "1234567890"


def get_neighbour_ids(i, j, rows, cols):
    return [
        (i + x, j + y)
        for x in [-1, 0, 1]
        for y in [-1, 0, 1]
        if not (x == 0 and y == 0) and 0 <= i + x < rows and 0 <= j + y < cols
    ]


def get_gear_value(i, j, engine_matrix):
    neighs = get_neighbour_ids(i, j, len(engine_matrix), len(engine_matrix[0]))
    nums = set()

    for ni, nj in neighs:
        if is_number(engine_matrix[ni][nj]):
            nums.add(extract_part_num(ni, nj, engine_matrix))

    return 0 if len(nums) != 2 else math.prod(nums)


def extract_part_num(i, j, engine_matrix):
    cols = len(engine_matrix[0])
    acc = [engine_matrix[i][j]]

    # Expand right
    idx = j + 1
    while 0 <= idx < cols and is_number(engine_matrix[i][idx]):
        acc = acc + [engine_matrix[i][idx]]
        idx += 1

    # Expand left
    idx = j - 1
    while 0 <= idx < cols and is_number(engine_matrix[i][idx]):
        acc = [engine_matrix[i][idx]] + acc
        idx -= 1

    return int("".join(acc))


def engine2(input_: str) -> int:
    engine_matrix = [list(line) for line in input_.split("\n")]
    rows, cols = len(engine_matrix), len(engine_matrix[0])

    acc = 0

    for i in range(rows):
        for j in range(cols):
            if engine_matrix[i][j] == "*":
                acc += get_gear_value(i, j, engine_matrix)

    return acc
