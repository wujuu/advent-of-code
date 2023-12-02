"""Part 1 of the https://adventofcode.com/2023/day/2"""

CONDITIONS = {"red": 12, "green": 13, "blue": 14}


def cubes1(input_: str) -> int:
    """Iter + check for conditions. Nothing fancy."""
    games = input_.split("\n")
    possible_games_acc = 0

    for game in games:
        header, actual_game = game.strip().split(":")
        game_no = int(header.strip().split()[1])
        handfuls = actual_game.strip().split(";")
        possible = True

        for handful in handfuls:
            cubes = handful.strip().split(",")

            for cube in cubes:
                amount, color = cube.strip().split()
                if int(amount) > CONDITIONS[color]:
                    possible = False

        if possible:
            possible_games_acc += game_no

    return possible_games_acc
