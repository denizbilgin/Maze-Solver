from typing import Union
from Node import Node
from Fringe import Fringe


class QueueFringe(Fringe):
    def __init__(self):
        super().__init__()

    def add(self, node: Node) -> None:
        self.fringe.append(node)

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            first_node: Node = self.fringe.pop(0)
            return first_node
