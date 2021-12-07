crabs = []


def median(numbers: list[int]) -> float:
    numbers = sorted(numbers)
    dataset_length = len(numbers)

    if dataset_length % 2 == 0:
        return (
            numbers[int(dataset_length / 2)] + numbers[int((dataset_length + 0.5) / 2)]
        ) / 2

    return numbers[int(dataset_length / 2)]


def fuel_used(pos: int) -> int:
    return sum(abs(pos - c) for c in crabs)


with open("day7_input.txt") as f:
    line = f.readline()
    crabs = line.rstrip().split(",")
    crabs = [int(c) for c in crabs]

med = median(crabs)
print(f"Median: {med}")
print(f"Fuel used: {fuel_used(med)}")
