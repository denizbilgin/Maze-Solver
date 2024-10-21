from typing import Union
from Node import Node
from Fringe import Fringe


class BreadthFirstSearch(Fringe):
    """
    Breadth-first search algorithm that uses queue.
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
            first_node: Node = self.fringe.pop(0)
            return first_node
