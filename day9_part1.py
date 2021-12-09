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

risk_levels = [floor[lp[0]][lp[1]] + 1 for lp in low_points]
sum_risk_levels = sum(risk_levels)

print(f"Risk levels Total: {sum_risk_levels}")
