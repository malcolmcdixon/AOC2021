NUM_BITS = 12

diagnostics = []

with open("day3_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        diagnostics.append(line.rstrip())

diag_as_ints = [int(d, 2) for d in diagnostics]

gamma = 0


def get_max_bit_count(bit: int) -> int:
    bit_value = 1 << bit
    count_of_1_bits = sum(1 for d in diag_as_ints if d & bit_value)
    return 1 if count_of_1_bits > (len(diag_as_ints) - count_of_1_bits) else 0


for bit in range(NUM_BITS):
    gamma |= 1 << bit if get_max_bit_count(bit) else 0

print(f"gamma: {gamma}")
epsilon = gamma ^ 2 ** NUM_BITS - 1
print(f"epsilon: {epsilon}")
print(f"answer: {gamma * epsilon}")
