
from typing import Union
from HeuristicFringe import HeuristicFringe
from Node import Node


class PriorityQueueFringe(HeuristicFringe):
    def __init__(self):
        super().__init__()

    def add(self, node: Node) -> None:
        node.heuristic = self.distance_to_goal(node)
        self.fringe.append(node)
        self.fringe.sort(key=lambda x: x.heuristic)

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            node: Node = self.fringe.pop(0)
            return node
