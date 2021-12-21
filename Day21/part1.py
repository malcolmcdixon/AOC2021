from typing import Iterator


import itertools


def roll_die(die: Iterator, times: int) -> tuple[int, int]:
    roll_die.counter += times
    return (sum(next(die) for _ in range(times)), roll_die.counter)


def move_player(players: list[int], player: int, spaces: int) -> int:
    for _ in range(spaces):
        space = next(players[player])
    return space


def main():
    die = itertools.cycle(range(1, 101))
    track = 10
    move = lambda: itertools.cycle(range(1, track + 1))
    roll_die.counter = 0
    players = [move(), move()]
    # set initial positions
    move_player(players, 0, 4)
    move_player(players, 1, 5)
    scores = [0, 0]

    player = 0
    while max(scores) < 1000:
        spaces_to_move, die_rolls = roll_die(die, 3)
        # print(spaces_to_move, die_rolls)
        scores[player] += move_player(players, player, spaces_to_move)
        player ^= 1

    print(f"Answer: {min(scores) * roll_die.counter}")


if __name__ == "__main__":
    main()
