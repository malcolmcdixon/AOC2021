crabs = []

with open("day7_input.txt") as f:
    line = f.readline()
    crabs = line.rstrip().split(",")
    crabs = sorted([int(c) for c in crabs])


def factorial(n: int) -> int:
    return n * (n + 1) / 2


mf = min(
    sum(factorial(abs(pos - c)) for c in crabs)
    for pos in range(min(crabs), max(crabs) + 1)
)

print(f"Min Fuel: {mf}")
