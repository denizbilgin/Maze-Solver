from Node import Node
from typing import Union


class StackFringe:
    def __init__(self):
        self.fringe: list[Node] = []

    def add(self, node: Node) -> None:
        self.fringe.append(node)

    def contains_state(self, state) -> bool:
        result: bool = any(node.state == state for node in self.fringe)
        return result

    def is_empty(self) -> bool:
        return len(self.fringe) == 0

    def remove(self) -> Union[Node, None]:
        if self.is_empty():
            raise Exception("Fringe is empty.")
        else:
            last_node: Node = self.fringe.pop()
            return last_node
