from Node import Node
from typing import Union, Tuple
from abc import ABC, abstractmethod


class Fringe(ABC):
    """
    Abstract base class for a fringe (or frontier) in search algorithms.

    This class represents a collection of nodes (states) that are used in search algorithms
    such as DFS, BFS, A*, and Uniform Cost Search. The fringe is responsible for managing
    the nodes that are waiting to be explored.
    """
    def __init__(self):
        self.fringe: list[Node] = []

    @abstractmethod
    def add(self, node: Node) -> None:
        """
        Adds a node to the fringe.

        This method must be implemented by subclasses and defines how nodes
        are added to the fringe (e.g., stack for DFS, queue for BFS).
        :param node: The node to be added to the fringe.
        :return: None
        """
        pass

    @abstractmethod
    def remove(self) -> Union[Node, None]:
        """
        Removes and returns a node from the fringe.

        This method must be implemented by subclasses and defines how nodes
        are removed from the fringe (e.g., last-in for DFS, first-in for BFS).
        :return: The node that is removed from the fringe, or None if the fringe is empty.
        """
        pass

    def contains_state(self, state: Tuple[int, int]) -> bool:
        """
        Checks whether the fringe contains a node with the given state.

        This method iterates over the nodes in the fringe to check if any node
        has a state that matches the given state.
        :param state: The state to check for in the fringe.
        :return: True if a node with the given state is found, False otherwise.
        """
        result: bool = any(node.state == state for node in self.fringe)
        return result

    def is_empty(self) -> bool:
        """
        Checks if the fringe is empty.
        :return: True if the fringe contains no nodes, False otherwise.
        """
        return len(self.fringe) == 0
