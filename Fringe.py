from Node import Node
from typing import Union, Tuple, List
from abc import ABC, abstractmethod


class Fringe(ABC):
    def __init__(self):
        self.fringe: list[Node] = []

    @abstractmethod
    def add(self, node: Node) -> None:
        pass

    @abstractmethod
    def remove(self) -> Union[Node, None]:
        pass

    def contains_state(self, state) -> bool:
        result: bool = any(node.state == state for node in self.fringe)
        return result

    def is_empty(self) -> bool:
        return len(self.fringe) == 0


class HeuristicFringe(Fringe, ABC):
    def __init__(self):
        super().__init__()
        self.fringe: List[Tuple[float, Node]] = []
        self.goal: Union[Tuple[int, int], None] = None
        self.distance_type: Union[str, None] = None

    def contains_state(self, state) -> bool:
        result: bool = any(node.state == state for _, node in self.fringe)
        return result

    def set_goal(self, goal: Tuple[int, int]):
        self.goal = goal

    def set_distance_type(self, distance_type: str):
        if distance_type not in ["manhattan", "euclidean", "diagonal"]:
            raise ValueError(f"Unknown distance type: {distance_type}")
        self.distance_type = distance_type

    def distance(self, node: Node) -> float:
        if self.goal is None:
            raise ValueError("Goal is not set.")

        current_state = node.state
        x1, y1 = current_state
        x2, y2 = self.goal

        if self.distance_type == "manhattan":
            return abs(x1 - x2) + abs(y1 - y2)
        elif self.distance_type == "euclidean":
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        elif self.distance_type == "diagonal":
            return max(abs(x1 - x2), abs(y1 - y2))
        else:
            raise ValueError(f"Unknown distance type: {self.distance_type}")