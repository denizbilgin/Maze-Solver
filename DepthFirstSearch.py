from Node import Node
from typing import Union
from Fringe import Fringe


class DepthFirstSearch(Fringe):
    """
    Depth-first search algorithm that uses stack.
    The algorithm is among the uninformed search algorithms.
    """
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
