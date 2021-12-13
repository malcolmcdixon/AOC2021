from PIL import Image


def get_input(filename: str) -> list[list[int]]:
    data = []
    with open(filename) as f:
        for line in f:
            x, y = line.rstrip().split(",")
            data.append([int(x), int(y)])
    return data


def get_folds(filename: str) -> list[tuple[str, int]]:
    data = []
    with open(filename) as f:
        for line in f:
            dir, fold_line = line.rstrip().split("=")
            dir = dir[-1]
            data.append((dir, int(fold_line)))
    return data


def translate(coord: int, fold_line: int) -> int:
    return abs(coord - fold_line * 2)


def fold_paper(paper: list[list[int]], dir: str, fold_line: int) -> list[list[int]]:
    folded_paper = paper.copy()

    for dot in paper:
        x, y = dot
        if dir == "y" and y > fold_line or dir == "x" and x > fold_line:
            if dir == "y":
                new_dot = [x, translate(y, fold_line)]
            else:
                new_dot = [translate(x, fold_line), y]

            if new_dot not in folded_paper:
                folded_paper.append(new_dot)

        if dir == "y" and y >= fold_line or dir == "x" and x >= fold_line:
            folded_paper.remove(dot)

    return folded_paper


def main():
    paper = get_input("Day13/input.txt")

    folds = get_folds("Day13/fold_instructions.txt")

    # part 1
    folded_paper = fold_paper(paper, *folds[0])
    print(f"Number of dots: {len(folded_paper)}")

    # part 2
    for fold in folds:
        paper = fold_paper(paper, *fold)

    max_x = max(dot[0] for dot in paper)
    max_y = max(dot[1] for dot in paper)

    image = Image.new(mode="RGB", size=(max_x + 1, max_y + 1))

    for dot in paper:
        x, y = dot
        image.putpixel((x, y), (255, 255, 255))

    image.show()


if __name__ == "__main__":
    main()
