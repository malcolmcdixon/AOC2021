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


lx, ly, ux, uy = target_area
num_hits = 0
for x in range(1, ux + 1):
    for y in range(uy, 1000):
        probe = (0, 0)
        velocity = (x, y)

        while True:
            px, py = probe
            vx, vy = velocity
            probe = (px + vx, py + vy)
            if check_in_target_area(probe, target_area):
                num_hits += 1
                break

            if missed_target_area(probe, target_area):
                break

            if vx:
                vx -= 1
            elif vx < 0:
                vx += 1

            vy -= 1

            velocity = (vx, vy)

print(f"Number of hits: {num_hits}")
