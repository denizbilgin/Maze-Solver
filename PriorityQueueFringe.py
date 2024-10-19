import heapq
from typing import Union
from Fringe import HeuristicFringe
from Node import Node


class PriorityQueueFringe(HeuristicFringe):
    def __init__(self):
        super().__init__()

    def add(self, node: Node) -> None:
        priority = self.distance(node)
        try:
            heapq.heappush(self.fringe, (priority, node))
        except TypeError:
            print("A")

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            _, node = heapq.heappop(self.fringe)
            return node
