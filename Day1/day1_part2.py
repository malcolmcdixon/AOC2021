depths = []

with open("day1_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        depths.append(int(line.rstrip()))


def sum3(idx):
    if idx + 2 > (len(depths) - 1):
        return 0
    return depths[idx] + depths[idx + 1] + depths[idx + 2]


result = sum(1 for idx, d in enumerate(depths) if idx and sum3(idx) > sum3(idx - 1))

print(result)
