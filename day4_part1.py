import math

drawn_numbers = [
    72,
    86,
    73,
    66,
    37,
    76,
    19,
    40,
    77,
    42,
    48,
    62,
    46,
    3,
    95,
    17,
    97,
    41,
    10,
    14,
    83,
    90,
    12,
    23,
    81,
    98,
    11,
    57,
    13,
    69,
    28,
    63,
    5,
    78,
    79,
    58,
    54,
    67,
    60,
    34,
    39,
    84,
    94,
    29,
    20,
    0,
    24,
    38,
    43,
    51,
    64,
    18,
    27,
    52,
    47,
    74,
    59,
    22,
    85,
    65,
    80,
    2,
    99,
    70,
    33,
    91,
    53,
    93,
    9,
    82,
    8,
    50,
    7,
    56,
    30,
    36,
    89,
    71,
    21,
    49,
    31,
    88,
    26,
    96,
    16,
    1,
    75,
    87,
    6,
    61,
    4,
    68,
    32,
    25,
    55,
    44,
    15,
    45,
    92,
    35,
]

cards = []

with open("day4_input.txt") as f:
    lines = f.readlines()
    line_count = 0
    for line in lines:
        line = line.rstrip()
        if line == "":
            continue
        line_numbers = line.split(" ")
        line_numbers = list(filter(lambda n: n != "", line_numbers))
        line_numbers = [int(n) for n in line_numbers]

        card_number = math.floor(line_count / 5)
        row = line_count % 5

        for col in range(5):
            cards.append([card_number, row, col, line_numbers[col], False])
        line_count += 1


def mark_cards(number: int) -> None:
    for c in cards:
        if c[3] == number:
            c[4] = True


def check_for_win() -> int:
    for card in range(math.floor(len(cards) / 5)):
        for row in range(5):
            num_of_nums = sum(1 for c in cards if c[0] == card and c[1] == row and c[4])
            if num_of_nums == 5:
                return card
        for col in range(5):
            num_of_nums = sum(1 for c in cards if c[0] == card and c[2] == col and c[4])
            if num_of_nums == 5:
                return card
    return -1


def get_card_unchecked_total(card: int) -> int:
    return sum(c[3] for c in cards if c[0] == card and c[4] == False)


for n in drawn_numbers:
    mark_cards(n)

    card = check_for_win()
    if card != -1:
        print("Card", card)
        print("WINNER NUMBER", n)
        print("Total Unchecked numbers", total := get_card_unchecked_total(card))
        print("Answer", n * total)
        break
