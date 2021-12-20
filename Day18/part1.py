import re
from enum import Enum


class ReduceType(Enum):
    EXPLODE = 0
    SPLIT = 1


def import_snailfish_numbers(file: str) -> list[str]:
    snailfish_numbers: list[str] = []
    with open(file) as f:
        for line in f:
            snailfish_numbers.append(line.rstrip())

    return snailfish_numbers


def get_previous_number(string: str, pos: int) -> tuple[int, int]:
    pattern = re.compile("\d+")
    result = pattern.finditer(string[:pos])
    results = [(int(m.group()), m.span()) for m in result]
    if results:
        return results[-1]

    return False, None


def get_next_number(string: str, pos: int) -> tuple[int, int]:
    pattern = re.compile("\d+")
    result = pattern.search(string, pos)
    if result:
        return (int(result.group()), result.span())

    return False, None


def addition(snf1: str, snf2: str) -> str:
    return f"[{snf1},{snf2}]"


def reduce_snailfish(
    snailfish: str, mode: ReduceType = ReduceType.EXPLODE
) -> tuple[bool, str]:
    open_brackets_pos: list[int] = []
    level = 0
    idx = 0
    explode = False
    while idx < len(snailfish):
        char = snailfish[idx]
        if char == ",":
            idx += 1
            continue
        if char == "[":
            open_brackets_pos.append(idx)
            level += 1
            explode = level >= 5
            idx += 1
            continue

        if char.isnumeric():
            number, span = get_next_number(snailfish, idx)

            if explode:
                # search for left number
                left, left_span = get_previous_number(snailfish, idx)
                if type(left) == int:
                    number += left
                    snailfish_left = snailfish[: left_span[0]]
                    snailfish_left += str(number) + snailfish[left_span[1] : idx - 1]
                else:
                    snailfish_left = snailfish[: idx - 1]

                # search for next number
                number, span = get_next_number(snailfish, span[1])
                idx = span[1] - 1

                # search for right number
                right, right_span = get_next_number(snailfish, idx + 1)
                if type(right) == int:
                    number += right
                    snailfish_right = snailfish[span[1] + 1 : right_span[0]]
                    snailfish_right += str(number) + snailfish[right_span[1] :]
                else:
                    snailfish_right = snailfish[span[1] + 1 :]

                snailfish = snailfish_left + "0" + snailfish_right

                return False, snailfish
            elif mode == ReduceType.SPLIT and number > 9:  # split
                left = number // 2
                right = (number + 1) // 2
                snailfish_left = snailfish[: span[0]]
                snailfish_right = snailfish[span[1] :]
                snailfish = f"{snailfish_left}[{left},{right}]{snailfish_right}"
                return False, snailfish
            else:
                idx = span[1]
                continue

        elif char == "]":
            open_brackets_pos.pop()
            level -= 1
            idx += 1

    return True, snailfish


def calculate_magnitude(match: re.Match) -> str:
    snf = match.group()[1:-1]
    span = match.span()
    left, right = map(int, snf.split(","))
    left *= 3
    right *= 2
    number = left + right
    return str(number)


def check_magnitude(snailfish: str) -> int:
    pattern = re.compile("\[\d+,\d+\]")
    while not snailfish.isdigit():
        snailfish = pattern.sub(calculate_magnitude, snailfish)
    return int(snailfish)


def main():
    snailfish_numbers: list[str] = import_snailfish_numbers("Day18/input.txt")

    snailfish = snailfish_numbers[0]

    for snailfish_number in snailfish_numbers[1:]:
        snailfish = addition(snailfish, snailfish_number)

        reduced = False
        while not reduced:
            exploded = False
            while not exploded:
                exploded, snailfish = reduce_snailfish(snailfish)

            reduced, snailfish = reduce_snailfish(snailfish, mode=ReduceType.SPLIT)

    # check magnitude
    answer = check_magnitude(snailfish)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
