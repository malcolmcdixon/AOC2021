from dataclasses import dataclass
import os
from PIL import Image


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
        self.end: Coordinate = Coordinate(0, 0)
        self.locations: dict[Coordinate, list[Vent]] = dict()
        self.dangerous_locations: list[Coordinate] = []
        self.most_dangerous_locations: list[Coordinate] = []
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
        if len(self.dangerous_locations) == 0:
            self.dangerous_locations = [
                loc for loc in self.locations if len(self.locations[loc]) > 1
            ]

        return self.dangerous_locations

    def most_dangerous_areas(self) -> list[Coordinate]:
        if len(self.most_dangerous_locations) == 0:
            max_vents = max(len(vents) for vents in self.locations.values())
            self.most_dangerous_locations = [
                loc for loc in self.locations if len(self.locations[loc]) == max_vents
            ]
        return self.most_dangerous_locations

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
                        self.add_vent_to_location(Coordinate(x, y), vent)

    def add_vent_to_location(self, coord: Coordinate, vent: Vent):
        location = self.locations.get(coord, None)
        if location is None:
            location = self.locations[coord] = []
        location.append(vent)

    def map_diag_vents(self):
        for vent in self.vents:
            x1 = vent.start.x
            y1 = vent.start.y
            x2 = vent.end.x
            y2 = vent.end.y

            d1 = abs(x1 - x2)
            d2 = abs(y1 - y2)

            if x1 != x2 and y1 != y2 and d1 == d2:
                # add start and end coordinates to locations
                x_dir = 1 if (x2 - x1) > 0 else -1
                y_dir = 1 if (y2 - y1) > 0 else -1

                for step in range(d1 + 1):
                    x = x1 + step * x_dir
                    y = y1 + step * y_dir

                    self.add_vent_to_location(Coordinate(x, y), vent)

    def draw(self) -> Image:
        img = Image.new(
            mode="RGB", size=(self.end.x + 1, self.end.y + 1), color=(206, 184, 136)
        )

        for loc in self.locations:
            color = (
                0,
                255,
                0,
            )

            img.putpixel((loc.x, loc.y), color)

        for loc in self.dangerous_areas():
            color = (
                255,
                191,
                0,
            )

            img.putpixel((loc.x, loc.y), color)

        for loc in self.most_dangerous_areas():
            color = (
                255,
                0,
                0,
            )

            img.putpixel((loc.x, loc.y), color)

        return img


def main():
    floor = Floor()

    with open("day5_input.txt") as f:
        lines = f.readlines()
        for line in lines:
            data = line.rstrip().split()
            x1, y1 = data[0].split(",")
            x2, y2 = data[2].split(",")
            vent = Vent(Coordinate(int(x1), int(y1)), Coordinate(int(x2), int(y2)))
            floor.add_vent(vent)

    floor.map_vents()
    floor.map_diag_vents()

    img = floor.draw()
    img.show()


if "__main__" in __name__:
    main()
