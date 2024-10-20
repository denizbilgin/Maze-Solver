from typing import Union
from Fringe import Fringe
from Node import Node


class UniformCostSearch(Fringe):
    """
    Uniform cost search algorithm that uses priority queue.
    The algorithm is among the uninformed search algorithms.
    """
    def __init__(self):
        super().__init__()

    def add(self, node: Node) -> None:
        self.fringe.append(node)
        self.fringe.sort(key=lambda x: x.cost)

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            first_node: Node = self.fringe.pop(0)
            return first_node
