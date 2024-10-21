from typing import Union
from Fringe import Fringe
from Node import Node


class HandSearch(Fringe):
    """
    Dummy hand rule search algorithm that uses stack or queue depending on selected hand.
    """
    def __init__(self, right_hand: bool = True):
        super().__init__()
        self.right_hand = right_hand

    def add(self, node: Node) -> None:
        self.fringe.append(node)

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            node: Node = self.fringe.pop(-1 if self.right_hand else 0)
            return node
