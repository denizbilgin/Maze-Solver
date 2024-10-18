from Node import Node
from typing import Union
from Fringe import Fringe


class StackFringe(Fringe):
    def __init__(self):
        super().__init__()

    def add(self, node: Node) -> None:
        self.fringe.append(node)

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            last_node: Node = self.fringe.pop()
            return last_node
