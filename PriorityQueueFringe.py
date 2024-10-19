import heapq
from typing import Union
from HeuristicFringe import HeuristicFringe
from Node import Node


class PriorityQueueFringe(HeuristicFringe):
    def __init__(self):
        super().__init__()

    def add(self, node: Node) -> None:
        heuristic = self.distance(node)
        node.heuristic = heuristic
        heapq.heappush(self.fringe, node)

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            node = heapq.heappop(self.fringe)
            return node
