from typing import Union
import os

octopuses = []
with open("day11_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data = [int(d) for d in line.rstrip()]
        octopuses.append(data)


def rc_generator() -> Union[int, int]:
    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            yield r, c


def adj_rc_generator(r, c) -> Union[int, int]:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if r + dy not in range(len(octopuses)) or c + dx not in range(
                len(octopuses[0])
            ):
                continue
            yield r + dy, c + dx


def increase_energy_levels() -> None:
    for r, c in rc_generator():
        octopuses[r][c] += 1


def increase_adj_energy_levels(row, col) -> None:
    for r, c in adj_rc_generator(row, col):
        if octopuses[r][c] < 10 or (r == row and c == col):
            octopuses[r][c] += 1


def reset_energy_levels() -> None:
    global flashes
    for r, c in rc_generator():
        if octopuses[r][c] > 9:
            flashes += 1
            octopuses[r][c] = 0


def do_step():
    increase_energy_levels()

    while True:
        to_flash_octopuses = sum(
            bool(o == 10) for o in [octopuses[r][c] for r, c in rc_generator()]
        )
        if to_flash_octopuses == 0:
            break

        for r, c in rc_generator():
            if octopuses[r][c] == 10:  # to flash
                increase_adj_energy_levels(r, c)

    # reset energy levels to 0
    reset_energy_levels()


def in_sync() -> bool:
    total = 0
    for octopus in octopuses:
        total += sum(octopus)
    return total == 0


# part 2
flashes = 0
step = 0
while not in_sync():
    do_step()
    step += 1

print(f"In sync at step: {step}")
