from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


class Cave:
    def __init__(self, name):
        self.name: str = name
        self._connections: list[Connection] = []
        self.visited: bool = False

    @property
    def connections(self) -> list[Connection]:
        return self._connections

    def add_connection(self, connection: Connection) -> None:
        # avoid connection to self
        if self != connection.connected_to:
            self._connections.append(connection)


@dataclass
class Path:
    start: str
    end: str


@dataclass
class Connection:
    connected_to: Cave


@dataclass
class Route:
    caves: list[Cave]


class CaveSystem:
    def __init__(self) -> CaveSystem:
        self.caves: dict[str, Cave] = {}
        self.paths: list[list[Cave]] = []

    def get_cave_by_name(self, name: str, create: bool = False) -> Optional[Cave]:
        cave = self.caves.get(name, None)

        if cave is None and create:
            cave = Cave(name)
            self.caves[name] = cave

        return cave

    def create_caves(self, paths: list[Path]) -> None:
        for path in paths:
            start_cave = self.get_cave_by_name(path.start, True)
            end_cave = self.get_cave_by_name(path.end, True)

            conn_s_e = Connection(end_cave)
            conn_e_s = Connection(start_cave)
            start_cave.add_connection(conn_s_e)
            end_cave.add_connection(conn_e_s)

    def find_paths(
        self, cave: Cave, end: Cave, visited: list[str] = [], route: list[str] = []
    ) -> None:
        route.append(cave.name)

        if cave.name.islower():
            visited.append(cave.name)

        if cave == end:
            self.paths.append(route)
            return

        for connection in cave.connections:
            cave = connection.connected_to

            if cave.name in visited:
                continue

            self.find_paths(cave, end, visited.copy(), route.copy())


def import_paths(file: str) -> list[Path]:
    paths: list[Path] = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            start, end = line.rstrip().split("-")

            paths.append(Path(start, end))

    return paths


def main():
    paths = import_paths("day12_input.txt")

    cave_system = CaveSystem()
    cave_system.create_caves(paths)

    start_cave = cave_system.get_cave_by_name("start")
    end_cave = cave_system.get_cave_by_name("end")

    cave_system.find_paths(start_cave, end_cave)

    print(f"Discrete Paths: {len(cave_system.paths)}")


if __name__ == "__main__":
    main()
