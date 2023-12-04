"""Part 1 of the https://adventofcode.com/2023/day/3"""


def is_symbol(char: str) -> bool:
    return char not in "1234567890."


def is_number(char: str) -> bool:
    return char in "1234567890"


def has_symbol_adj(i, j, engine_matrix):
    rows, cols = len(engine_matrix), len(engine_matrix[0])

    neighbour_ids = [
        (i + x, j + y)
        for x in [-1, 0, 1]
        for y in [-1, 0, 1]
        if not (x == 0 and y == 0) and 0 <= i + x < rows and 0 <= j + y < cols
    ]

    return any(is_symbol(engine_matrix[ni][nj]) for ni, nj in neighbour_ids)


def sum_valid_part_numbers(engine_matrix, valid_parts_mask) -> int:
    acc = 0

    for i in range(len(engine_matrix)):
        row, mask = engine_matrix[i], valid_parts_mask[i]
        row_masked = [char if mask else " " for char, mask in zip(row, mask)]
        acc += sum(int(num) for num in "".join(row_masked).split() if num)

    return acc


def engine1(input_: str) -> int:
    engine_matrix = [list(line) for line in input_.split("\n")]
    rows, cols = len(engine_matrix), len(engine_matrix[0])
    valid_parts_mask = [[False for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if is_number(engine_matrix[i][j]) and has_symbol_adj(i, j, engine_matrix):
                valid_parts_mask[i][j] = True

                # Expand right
                idx = j + 1
                while 0 <= idx < cols and is_number(engine_matrix[i][idx]):
                    valid_parts_mask[i][idx] = True
                    idx += 1

                # Expand left
                idx = j - 1
                while 0 <= idx < cols and is_number(engine_matrix[i][idx]):
                    valid_parts_mask[i][idx] = True
                    idx -= 1

    return sum_valid_part_numbers(engine_matrix, valid_parts_mask)
