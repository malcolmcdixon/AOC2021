crabs = []

with open("day7_input.txt") as f:
    line = f.readline()
    crabs = line.rstrip().split(",")
    crabs = sorted([int(c) for c in crabs])


def factorial(n: int) -> int:
    return n * (n + 1) / 2


min_fuel = factorial(max(crabs) - min(crabs)) * len(crabs)
for pos in range(min(crabs), max(crabs) + 1):
    fuel_used = sum(factorial(abs(pos - c)) for c in crabs)
    if fuel_used < min_fuel:
        min_fuel = fuel_used
        print(pos, min_fuel)
