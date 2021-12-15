digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "bcdf",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

signals = []
outputs = []

unique_digits = [1, 4, 7, 8]

with open("day8_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data = line.rstrip().split()
        signals.append(data[:9])
        outputs.append(data[-4:])


def unique_digit_instances_in_outputs() -> int:
    unique_digit_lengths = [len(digits[ud]) for ud in unique_digits]
    return sum(
        sum(bool(len(value) in unique_digit_lengths) for value in output)
        for output in outputs
    )


print(unique_digit_instances_in_outputs())
