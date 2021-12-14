from collections import Counter


def get_pair_insertions(filename: str) -> list[list[int]]:
    data = {}
    with open(filename) as f:
        for line in f:
            element_pair, element = line.rstrip().split(" -> ")
            data[element_pair] = element
    return data


def find_optimal_polymer_formula(
    polymer_template: str, pair_insertions: dict[str, str], steps: int
) -> str:
    for _ in range(steps):
        new_polymer_template = polymer_template[0]
        for pos in range(len(polymer_template) - 1):
            pair_insertion = polymer_template[pos : pos + 2]
            new_polymer_template += (
                pair_insertions[pair_insertion] + polymer_template[pos + 1]
            )

        polymer_template = new_polymer_template

    return polymer_template


def main():
    polymer_template = "COPBCNPOBKCCFFBSVHKO"
    pair_insertions = get_pair_insertions("Day14/input.txt")

    optimal_polymer_formula = find_optimal_polymer_formula(
        polymer_template, pair_insertions, 10
    )

    print(len(optimal_polymer_formula))

    element_counts = Counter(optimal_polymer_formula)

    most_common = max(element_counts.values())
    least_common = min(element_counts.values())

    print(f"Most less Least: {most_common - least_common}")


if __name__ == "__main__":
    main()
