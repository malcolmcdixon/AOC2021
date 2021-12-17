from __future__ import annotations
from dataclasses import dataclass
from os import write
from typing import Optional


class Node:
    def __init__(self, name):
        self.name: str = name
        self._connections: list[Connection] = []
        self.risk: float = float("inf")
        self._via: Optional[Node] = None

    @property
    def connections(self) -> list[Connection]:
        return self._connections

    @property
    def via(self) -> Optional[Node]:
        return self._via

    @via.setter
    def via(self, node: Node) -> None:
        if self == node:
            raise ValueError("Cannot set via to self")
        self._via = node

    def __eq__(self, other: Node) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def add_connection(self, connection: Connection) -> None:
        # avoid connection to self
        if self != connection.connected_to:
            self._connections.append(connection)


@dataclass
class Connection:
    connected_to: Node
    risk: float


@dataclass
class Path:
    start: str
    end: str
    risk: int


class Graph:
    def __init__(self) -> Graph:
        self.nodes: dict[str, Node] = {}

    def get_node_by_name(self, name: str, create: bool = False) -> Optional[Node]:
        node = self.nodes.get(name, None)

        if node is None and create:
            node = Node(name)
            self.nodes[name] = node

        return node

    def create_nodes(self, paths: list[Path]) -> None:
        for path in paths:
            start_node = self.get_node_by_name(path.start, True)
            end_node = self.get_node_by_name(path.end, True)

            risk = path.risk
            conn_s_e = Connection(end_node, risk)
            start_node.add_connection(conn_s_e)

    def find_best_route(self, start: str, end: str) -> Optional[list[Node]]:
        completed: set[Node] = set()
        start_node = self.get_node_by_name(start)
        if start_node is None:
            return None
        start_node.risk = 0
        end_node = self.get_node_by_name(end)
        if end_node is None:
            return None

        priority_list: list[Node] = [start_node]

        while True:
            # sort nodes by risk, shortest at end, pop() much quicker at end of array
            priority_list.sort(reverse=True, key=lambda node: node.risk)
            node = priority_list.pop()

            # reached end node, must be shortest route
            if node == end_node:
                completed.add(node)
                break

            for connection in node.connections:
                # if node already visited process next connection
                if connection.connected_to in completed:
                    continue

                # get connected to's node
                ct_node = connection.connected_to

                # update risk and via
                risk = node.risk + connection.risk
                if risk <= ct_node.risk:
                    ct_node.risk = risk
                    ct_node.via = node
                    if ct_node not in priority_list:
                        priority_list.append(ct_node)

            completed.add(node)

        route = []
        node = end_node
        while node:
            route.append(node)
            node = node.via

        route.sort(key=lambda node: node.risk)

        return route


def import_risks(file: str) -> list[str]:
    risks = []
    with open(file) as f:
        for line in f:
            risks.append(line.rstrip())

    return risks


def extend_risks(risks: list[str], shape: int) -> list[str]:
    extended_risks = [""] * shape * 5
    for row in range(5):
        for risk_row in range(shape):
            new_row = shape * row + risk_row
            new_risks = ""
            for col in range(5):
                for risk in risks[risk_row]:
                    new_risk = int(risk) + row + col
                    new_risks += str(new_risk if new_risk < 10 else new_risk - 9)

            extended_risks[new_row] = new_risks

    return extended_risks


def export_extended_risks(file: str, extended_risks: list[list[int]]) -> None:
    with open(file, "w") as f:
        for er in extended_risks:
            f.write(f"{er}\n")


def import_paths(file: str) -> list[Path]:
    paths: list[Path] = []
    prev_cols = ""
    with open(file) as f:
        for row, line in enumerate(f):
            cols = line.rstrip()
            for col, risk in enumerate(cols):
                # right, left
                if col > 0:
                    start = f"{row},{col - 1}"
                    end = f"{row},{col}"
                    paths.append(Path(start, end, int(risk)))
                    paths.append(Path(end, start, int(cols[col - 1])))
                # down, up
                if row > 0:
                    start = f"{row-1},{col}"
                    end = f"{row},{col}"
                    paths.append(Path(start, end, int(risk)))
                    paths.append(Path(end, start, int(prev_cols[col])))
            prev_cols = cols

    return paths


def main():
    risks = import_risks("Day15/input.txt")

    extended_risks = extend_risks(risks, shape=100)

    export_extended_risks("Day15/extended_input.txt", extended_risks)

    paths = import_paths("Day15/extended_input.txt")

    print(f"Paths: {len(paths)}")

    graph = Graph()
    graph.create_nodes(paths)

    node_names = list(graph.nodes.keys())

    start = "0,0"
    end = node_names[-1]

    route = graph.find_best_route(start, end)

    print(route[-1].name, route[-1].risk)


if __name__ == "__main__":
    main()
