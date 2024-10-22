from abc import ABC
from typing import Union, Tuple
from Fringe import Fringe
from Node import Node


class HeuristicFringe(Fringe, ABC):
    """
    Abstract base class for a heuristic-based fringe (frontier) in informed search algorithms.

    This class extends the `Fringe` class by adding heuristic capabilities, such as calculating
    the distance from a node to the goal state using different distance metrics (e.g., Manhattan, Euclidean, Diagonal).
    """
    __distance_types: list[str] = ["manhattan", "euclidean", "diagonal"]

    def __init__(self):
        super().__init__()
        self.goal_state: Union[Tuple[int, int], None] = None
        self.distance_type: Union[str, None] = None

    def set_distance_type(self, distance_type: str) -> None:
        """
        Sets the type of distance metric for heuristic calculations.

        The available distance types are: 'manhattan', 'euclidean', and 'diagonal'.
        If an unsupported distance type is provided, a ValueError is raised.
        :param distance_type: The type of distance metric to use (case-insensitive).
        :return: None
        """
        distance_type = distance_type.lower()
        if distance_type not in self.__distance_types:
            raise ValueError(f"Unknown distance type: {distance_type}. You can use these distances: {self.__distance_types}")
        self.distance_type = distance_type

    def distance_to_goal(self, node: Node) -> float:
        """
        Calculates the heuristic distance between the current node and the goal state.

        The method calculates the distance based on the distance type set by `set_distance_type`.
        If the goal state is not set, it raises a ValueError.

        Supported distance types are:
        - Manhattan: Sum of the absolute differences of x and y coordinates.
        - Euclidean: Straight-line distance between two points.
        - Diagonal: Maximum of the absolute differences of x and y coordinates.
        :param node: The node for which the distance to the goal state is being calculated.
        :return: The heuristic distance from the current node to the goal state.
        """
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
