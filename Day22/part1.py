def import_reboot_steps(file: str) -> list[str]:
    reboot_steps: list[str] = []
    with open(file) as f:
        for line in f:
            reboot_steps.append(line.rstrip())

    return reboot_steps


def parse_reboot_step(step: str) -> tuple[bool, tuple[list[int]]]:
    state, cubes = step.split(" ")
    x, y, z = cubes.split(",")

    x_range = list(map(int, x.replace("x=", "").split("..")))
    y_range = list(map(int, y.replace("y=", "").split("..")))
    z_range = list(map(int, z.replace("z=", "").split("..")))

    return (state == "on", (x_range, y_range, z_range))


def range_in_bounds(n_range: list[int], bounds: tuple[int]) -> list[int]:
    lower = bounds[0]
    upper = bounds[1]
    lower_range = n_range[0]
    upper_range = n_range[1]
    return [max(lower, lower_range), min(upper, upper_range)]


def generate_cuboid(ranges: tuple[list[int]], bounds: tuple[int]) -> set[tuple[int]]:
    x_range, y_range, z_range = ranges
    x_range = range_in_bounds(x_range, bounds)
    y_range = range_in_bounds(y_range, bounds)
    z_range = range_in_bounds(z_range, bounds)
    for x in range(x_range[0], x_range[1] + 1):
        for y in range(y_range[0], y_range[1] + 1):
            for z in range(z_range[0], z_range[1] + 1):
                yield (x, y, z)


def main():

    reactor_core = set()

    reboot_steps = import_reboot_steps("Day22/input.txt")

    bounds = (-50, 50)

    for step in reboot_steps:
        state, ranges = parse_reboot_step(step)

        for cube in generate_cuboid(ranges, bounds):
            if state:  # switch on
                reactor_core.add(cube)
            else:  # switch off
                reactor_core.discard(cube)

    print(f"Answer: {len(reactor_core)}")


if __name__ == "__main__":
    main()
