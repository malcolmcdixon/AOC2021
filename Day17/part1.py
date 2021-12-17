target_area = (25, -200, 67, -260)


def check_in_target_area(
    probe: tuple[int, int], target_area: tuple[int, int, int, int]
) -> bool:
    px, py = probe
    lx, ly, ux, uy = target_area
    return lx <= px <= ux and uy <= py <= ly


def missed_target_area(
    probe: tuple[int, int], target_area: tuple[int, int, int, int]
) -> bool:
    px, py = probe
    lx, ly, ux, uy = target_area
    return px > ux or py < uy


probe_max_heights = []
lx, ly, ux, uy = target_area
for x in range(1, ux + 1):
    for y in range(uy, 1000):
        probe = (0, 0)
        velocity = (x, y)
        probe_heights = []

        while True:
            px, py = probe
            vx, vy = velocity
            probe = (px + vx, py + vy)
            probe_heights.append(py + vy)
            if check_in_target_area(probe, target_area):
                probe_max_heights.append(max(probe_heights))

            if missed_target_area(probe, target_area):
                break

            if vx:
                vx -= 1
            elif vx < 0:
                vx += 1

            vy -= 1

            velocity = (vx, vy)

print(f"Max height: {max(probe_max_heights)}")
