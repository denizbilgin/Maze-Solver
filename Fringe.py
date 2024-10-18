from Node import Node
from typing import Union, Tuple
from abc import ABC, abstractmethod


class Fringe(ABC):
    def __init__(self):
        self.fringe: list[Node] = []

    @abstractmethod
    def add(self, node: Node) -> None:
        pass

    def contains_state(self, state) -> bool:
        result: bool = any(node.state == state for node in self.fringe)
        return result

    def is_empty(self) -> bool:
        return len(self.fringe) == 0

    @abstractmethod
    def remove(self) -> Union[Node, None]:
        pass


class HeuristicFringe(Fringe, ABC):
    def __init__(self):
        super().__init__()
        self.goal = None
        self.distance_type = None

    def set_goal(self, goal: Tuple[int, int]):
        self.goal = goal

    def distance(self, node: Node) -> float:
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
