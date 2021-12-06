from collections import Counter

DAYS = 256
FISH_START = 6
NEW_FISH_START = 8

with open("day6_input.txt") as f:
    line = f.readline()
    fish = line.rstrip().split(",")
    fish = [int(f) for f in fish]

# create initial schools
fish_count = Counter(fish)
schools = [[timer, fish] for timer, fish in fish_count.items()]

for day in range(DAYS):
    # reduce schools internal timer
    for school in schools:
        school[0] -= 1

    number_of_new_fish = sum(school[1] for school in schools if school[0] == -1)

    if number_of_new_fish:
        # restart elapsed internal timers
        for school in schools:
            if school[0] == -1:
                school[0] = FISH_START

        # add new school
        new_school = [[NEW_FISH_START, number_of_new_fish]]
        schools += new_school

    number_of_fish = sum(school[1] for school in schools)
    print(f"Day: {day + 1} - {number_of_fish}")
