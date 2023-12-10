def distance(time_held, race_duration) -> int:
    assert 0 < time_held < race_duration
    time_left = race_duration - time_held
    return time_held * time_left


def boat_race1(input_: str) -> int:
    """Brute force solution. More interesting one is in the part2."""
    race_durations_raw, record_distances_raw = input_.split("\n")
    race_durations, record_dists = (
        map(int, race_durations_raw.split()[1:]),
        map(int, record_distances_raw.split()[1:]),
    )

    res_acc = 1

    for race_duration, record_dist in zip(race_durations, record_dists):
        res_acc *= sum(
            distance(time_held, race_duration) > record_dist
            for time_held in range(1, race_duration)
        )

    return res_acc
