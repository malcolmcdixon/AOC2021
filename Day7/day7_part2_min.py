with open("day7_input.txt") as f:
    line = f.readline()
    crabs = sorted(map(lambda x: int(x), line.rstrip().split(",")))

mf = min(
    sum(abs(pos - c) * (abs(pos - c) + 1) / 2 for c in crabs)
    for pos in range(min(crabs), max(crabs) + 1)
)

print(f"Min Fuel: {mf}")
