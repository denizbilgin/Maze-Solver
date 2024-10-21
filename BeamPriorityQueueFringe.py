from typing import Union
from HeuristicFringe import HeuristicFringe
from Node import Node


class BeamPriorityQueueFringe(HeuristicFringe):
    def __init__(self, beam_width: int = 3, distance_type: str = "manhattan"):
        super().__init__()
        self.beam_width = beam_width
        self.set_distance_type(distance_type)

    def add(self, node: Node) -> None:
        node.heuristic = self.distance_to_goal(node)
        self.fringe.append(node)
        self.fringe.sort(key=lambda x: x.cost + x.heuristic)

        if len(self.fringe) > self.beam_width:
            self.fringe = self.fringe[:self.beam_width]

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            first_node: Node = self.fringe.pop(0)
            return first_node
