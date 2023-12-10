import numpy as np


def boat_race2(input_: str) -> int:
    """This solution solves the question by seeing that the distance function can be
    represented as a quadratic equation:

    distance_traveled(time_held) = -1 * time_held**2 + race_duration * time_held  - record_dist

    We then solve for the roots for this equation and just count how many natural positive number
    are contained between the roots
    """
    race_durations_raw, record_distances_raw = input_.split("\n")
    race_duration, record_dist = (
        int("".join(race_durations_raw.split()[1:])),
        int("".join(record_distances_raw.split()[1:])),
    )

    polynomial_params = [-1, race_duration, -record_dist]

    bigger_root, smaller_root = np.roots(polynomial_params)
    return int(np.floor(bigger_root)) - int(np.ceil(smaller_root)) + 1
