import numpy as np


def convert_image_data_to_binary_string(data: str) -> int:
    data = data.replace(".", "0")
    data = data.replace("#", "1")

    return data


def import_image_enhancement_algorithm(file: str) -> int:
    with open(file) as f:
        iea = f.readline().rstrip()

    iea = convert_image_data_to_binary_string(iea)

    return iea


def import_input_image(file: str) -> np.array:
    converted_file = f"{file[:-4]}_converted.txt"
    with open(converted_file, "w") as output:
        with open(file) as f:
            for line in f:
                converted_line = convert_image_data_to_binary_string(line.rstrip())
                output.write(f"{' '.join(converted_line)}\n")

    return np.loadtxt(converted_file, dtype=int)


def combine_3x3_pixels_into_binary_string(array: np.array, pos: tuple[int, int]) -> str:
    r, c = pos
    pixels_3x3 = array[r - 1 : r + 2, c - 1 : c + 2].flatten()

    return "".join(map(str, pixels_3x3))


def enhance_image(input: np.array, iea: str) -> np.array:
    output = np.zeros(shape=input.shape, dtype=int)

    for r in range(1, input.shape[0] - 1):
        for c in range(1, input.shape[1] - 1):
            binary_number = combine_3x3_pixels_into_binary_string(input, (r, c))
            number = int(binary_number, 2)
            pixel = iea[number]
            output[(r, c)] = pixel

    return output


def expand_image(input: np.array, fill: int) -> np.array:
    # shrink first to bounds where there's a lit pixel (1)
    result = np.where(input == 1)
    r_min = np.amin(result[0])
    r_max = np.amax(result[0])
    c_min = np.amin(result[1])
    c_max = np.amax(result[1])

    input = input[r_min : r_max + 1, c_min : c_max + 1]

    return np.pad(input, 10, mode="constant", constant_values=fill)


def main():
    iea = import_image_enhancement_algorithm("Day20/input.txt")

    input_image = import_input_image("Day20/image_input.txt")

    input_image = expand_image(input_image, 0)

    output_image = enhance_image(input_image, iea)

    input_image = expand_image(output_image, 1)

    output_image = enhance_image(input_image, iea)

    print(f"No. of elements: {np.sum(output_image)}")


if __name__ == "__main__":
    main()
