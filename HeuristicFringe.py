from abc import ABC
from typing import Union, Tuple
from Fringe import Fringe
from Node import Node


class HeuristicFringe(Fringe, ABC):
    __distance_types: list[str] = ["manhattan", "euclidean", "diagonal"]

    def __init__(self):
        super().__init__()
        self.goal_state: Union[Tuple[int, int], None] = None
        self.distance_type: Union[str, None] = None

    def set_distance_type(self, distance_type: str) -> None:
        distance_type = distance_type.lower()
        if distance_type not in self.__distance_types:
            raise ValueError(f"Unknown distance type: {distance_type}. You can use these distances: {self.__distance_types}")
        self.distance_type = distance_type

    def distance_to_goal(self, node: Node) -> float:
        if self.goal_state is None:
            raise ValueError("Goal is not set. You need to set goal first.")

        current_state = node.state
        x1, y1 = current_state
        x2, y2 = self.goal_state

        if self.distance_type == "manhattan":
            return abs(x1 - x2) + abs(y1 - y2)
        elif self.distance_type == "euclidean":
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        elif self.distance_type == "diagonal":
            return max(abs(x1 - x2), abs(y1 - y2))
        else:
            return -1
