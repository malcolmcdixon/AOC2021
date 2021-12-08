digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

segments = [c for c in "abcdefg"]

signals = []
outputs = []

unique_digits = [1, 4, 7, 8]

with open("day8_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data = line.rstrip().split()
        signals.append(data[:10])
        outputs.append(data[-4:])


udl = {ud: len(digits[ud]) for ud in unique_digits}


def key_by_value(items: dict, value: int) -> int:
    for k, v in items.items():
        if v == value:
            return k


def sort_string(str1: str) -> str:
    return "".join(sorted(str1))


def xor_string(str1: str, str2: str) -> str:
    result1 = [c for c in str1 if c not in str2]
    result2 = [c for c in str2 if c not in str1]
    return sort_string("".join(result1 + result2))


def and_string(str1: str, str2: str) -> str:
    return sort_string("".join([c for c in str1 if c in str2]))


total = 0

for signal, output in zip(signals, outputs):
    mapping = {}
    signal.sort(key=len)

    for pattern in signal:
        if len(pattern) in [5, 6]:
            continue

        pattern = sort_string(pattern)

        # known number
        digit = key_by_value(udl, len(pattern))
        mapping[digit] = pattern

    xor_4_8 = xor_string(mapping[4], mapping[8])

    for pattern in signal:
        if len(pattern) not in [5, 6]:
            continue

        pattern = sort_string(pattern)

        if len(pattern) == 5:
            if and_string(pattern, mapping[1]) == mapping[1]:
                mapping[3] = pattern
            elif and_string(pattern, xor_4_8) == xor_4_8:
                mapping[2] = pattern
            else:
                mapping[5] = pattern

        else:  # len == 6
            if and_string(pattern, mapping[1]) != mapping[1]:
                mapping[6] = pattern
            else:
                xor_with_4 = xor_string(pattern, mapping[4])
                if len(xor_with_4) == 2:
                    mapping[9] = pattern
                else:
                    mapping[0] = pattern

    output_value = 0
    for idx, code in enumerate(output):
        code = sort_string(code)
        digit = key_by_value(mapping, code)
        output_value += digit * 10 ** (3 - idx)

    total += output_value

print(total)
