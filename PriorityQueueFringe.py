
from typing import Union
from HeuristicFringe import HeuristicFringe
from Node import Node


class PriorityQueueFringe(HeuristicFringe):
    def __init__(self, distance_type: str = "manhattan"):
        super().__init__()
        self.set_distance_type(distance_type)

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
