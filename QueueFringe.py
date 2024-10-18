from typing import Union
from Node import Node
from StackFringe import StackFringe


class QueueFringe(StackFringe):
    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            first_node: Node = self.fringe.pop(0)
            return first_node
        