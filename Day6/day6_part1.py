DAYS = 80
FISH_START = 6
NEW_FISH_START = 8
fish = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,
    1,
    2,
    1,
    1,
    4,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    2,
    1,
    2,
    1,
    3,
    3,
    4,
    1,
    4,
    1,
    1,
    3,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    4,
    1,
    1,
    5,
    1,
    1,
    1,
    4,
    1,
    5,
    1,
    1,
    1,
    3,
    1,
    1,
    5,
    3,
    1,
    1,
    1,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    2,
    4,
    1,
    1,
    1,
    1,
    4,
    1,
    2,
    2,
    1,
    1,
    1,
    3,
    1,
    2,
    5,
    1,
    4,
    1,
    1,
    1,
    3,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    1,
    1,
    5,
    1,
    1,
    1,
    4,
    1,
    1,
    5,
    1,
    1,
    5,
    3,
    3,
    5,
    3,
    1,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    3,
    1,
    2,
    1,
    1,
    1,
    4,
    1,
    3,
    1,
    5,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    4,
    3,
    2,
    1,
    2,
    4,
    1,
    3,
    1,
    5,
    1,
    2,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    4,
    1,
    1,
    1,
    1,
    3,
    1,
    3,
    3,
    1,
    4,
    3,
    4,
    1,
    1,
    1,
    1,
    5,
    1,
    3,
    3,
    2,
    5,
    3,
    1,
    1,
    3,
    1,
    3,
    1,
    1,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    3,
    1,
    5,
    1,
    1,
    1,
    4,
    4,
    1,
    1,
    5,
    5,
    2,
    4,
    5,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    2,
    1,
    1,
]


for _ in range(DAYS):
    # reduce internal timer
    fish = [f - 1 for f in fish]
    # add new fish
    number_of_new_fish = sum(1 for f in fish if f == -1)
    new_fish = [NEW_FISH_START] * number_of_new_fish
    fish += new_fish
    # restart elapsed internal timers
    fish = [FISH_START if f == -1 else f for f in fish]

print(f"Answer: {len(fish)}")