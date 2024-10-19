from Node import Node
from typing import Union
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
