from typing import Union
from Fringe import Fringe
from Node import Node


class IterativeDeepeningStackFringe(Fringe):
    def __init__(self, depth_limit: int = 15):
        super().__init__()
        self.__set_depth_limit(depth_limit)

    def __set_depth_limit(self, depth_limit: int):
        if depth_limit < 1:
            raise ValueError("Depth limit must be set greater than 0.")
        self.depth_limit = depth_limit

    def add(self, node: Node) -> None:
        if self.depth_limit is not None:
            if node.cost <= self.depth_limit:
                self.fringe.append(node)
        else:
            raise ValueError("Depth limit must be set.")

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            node: Node = self.fringe.pop()
            return node
