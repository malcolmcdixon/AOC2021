floor = []
with open("day9_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        data = [int(d) for d in line.rstrip()]
        floor.append(data)

low_points = []

for row in range(len(floor)):
    for col in range(len(floor[0])):
        if floor[row][col] == 9:
            continue
        low_point = True
        for x_pos in range(-1, 2):
            if not low_point:
                break
            for y_pos in range(-1, 2):
                if abs(x_pos) == abs(y_pos):
                    continue
                if 0 <= row + y_pos < len(floor) and 0 <= col + x_pos < len(floor[0]):
                    if floor[row][col] >= floor[row + y_pos][col + x_pos]:
                        low_point = False
                        break
        if low_point:
            low_points.append([row, col])


def basin(point: list[int], basin_points: list[int]) -> int:
    if point not in basin_points:
        basin_points.append(point)
    row = point[0]
    col = point[1]
    for x_pos in range(-1, 2):
        for y_pos in range(-1, 2):
            if abs(x_pos) == abs(y_pos):
                continue
            if 0 <= row + y_pos < len(floor) and 0 <= col + x_pos < len(floor[0]):
                if floor[row + y_pos][col + x_pos] == 9:
                    continue
                if floor[row][col] < floor[row + y_pos][col + x_pos]:
                    basin_points = basin([row + y_pos, col + x_pos], basin_points)

    return basin_points


basin_sizes = [len(basin(lp, [])) for lp in low_points]
basin_sizes.sort(reverse=True)

largest_3_basins_multiplied = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(largest_3_basins_multiplied)
