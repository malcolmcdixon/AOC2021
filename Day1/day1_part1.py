depths = []

with open("day1_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        depths.append(int(line.rstrip()))

result = sum(1 for idx, d in enumerate(depths) if idx and d > depths[idx - 1])

print(result)
