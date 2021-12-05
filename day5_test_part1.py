from dataclasses import dataclass
import os


@dataclass
class Coordinate:
    x: int
    y: int

    def __key(self):
        return (self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.__key() == other.__key()
        return NotImplemented

    def __hash__(self):
        return hash(self.__key())


@dataclass
class Vent:
    start: Coordinate
    end: Coordinate


class Floor:
    def __init__(self):
        self.start: Coordinate = Coordinate(0, 0)
        self.end: Coordinate = Coordinate(9, 9)
        self.locations: dict[Coordinate, list[Vent]] = dict()
        self.vents: list[Vent] = list()

    def add_vent(self, vent: Vent) -> None:
        self.vents.append(vent)
        # set end coordinates
        max_x = max(vent.start.x, vent.end.x)
        max_y = max(vent.start.y, vent.end.y)
        if max_x > self.end.x:
            self.end.x = max_x
        if max_y > self.end.y:
            self.end.y = max_y

    def dangerous_areas(self) -> list[Coordinate]:
        return [l for l in self.locations.values() if len(l) > 1]

    def map_vents(self):
        for vent in self.vents:
            x1 = vent.start.x
            y1 = vent.start.y
            x2 = vent.end.x
            y2 = vent.end.y
            if x1 == x2 or y1 == y2:
                # update ocean floor locations
                startx = min(x1, x2)
                endx = max(x1, x2)
                starty = min(y1, y2)
                endy = max(y1, y2)
                for x in range(startx, endx + 1):
                    for y in range(starty, endy + 1):
                        location = self.locations.get(Coordinate(x, y), None)
                        if location is None:
                            location = self.locations[Coordinate(x, y)] = []
                        location.append(vent)

    def draw(self):
        for y in range(self.start.y, self.end.y + 1):
            line = ["."] * (self.end.x + 1)

            for x in range(self.start.x, self.end.x + 1):
                location = self.locations.get(Coordinate(x, y), None)
                if location is None:
                    continue

                line[x] = str(len(location))

            print("".join(line))


def main():
    floor = Floor()

    with open("day5_test_input.txt") as f:
        lines = f.readlines()
        for line in lines:
            data = line.rstrip().split()
            x1, y1 = data[0].split(",")
            x2, y2 = data[2].split(",")
            vent = Vent(Coordinate(int(x1), int(y1)), Coordinate(int(x2), int(y2)))
            floor.add_vent(vent)

    floor.map_vents()

    os.system("cls")
    floor.draw()

    danger_areas = floor.dangerous_areas()

    print(f"Answer: {len(danger_areas)}")


if "__main__" in __name__:
    main()
