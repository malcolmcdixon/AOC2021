NUM_BITS = 12
OXYGEN = 1
CO2 = 0

diagnostics = []

with open("day3_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        diagnostics.append(line.rstrip())

diag_as_ints = [int(d, 2) for d in diagnostics]


def get_max_bit_count(diags: list[int], bit: int) -> int:
    bit_value = 1 << bit
    count_of_1_bits = sum(1 for d in diags if d & bit_value)
    return count_of_1_bits, len(diags) - count_of_1_bits


def reduce_diags(diags: list[int], bit: int, sig_bit: int) -> list[int]:
    bit_1s, bit_0s = get_max_bit_count(diags, bit)
    print(bit_1s, bit_0s)

    if bit_1s > bit_0s:
        max_bits = 1 & sig_bit
    elif bit_1s == bit_0s:
        max_bits = sig_bit
    else:
        max_bits = not (0 | sig_bit)
    print(max_bits)

    diags = [d for d in diags if (d & (1 << bit)) >> bit == max_bits]
    if len(diags) == 2 or bit == 0:
        diags = [d for d in diags if d & 1 == sig_bit]
        return diags
    elif len(diags) == 1:
        return diags

    return reduce_diags(diags, bit - 1, sig_bit)


oxygen = reduce_diags(diag_as_ints, NUM_BITS - 1, OXYGEN)
print(f"oxygen: {oxygen}")

co2 = reduce_diags(diag_as_ints, NUM_BITS - 1, CO2)
print(f"CO2: {co2}")

print(f"life support:{oxygen[0] * co2[0]}")
