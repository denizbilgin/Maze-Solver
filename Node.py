from typing import Tuple, Union


class Node:
    def __init__(self, state: Tuple[int, int], parent: Union["Node", None], action: Union[str, None]):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic: Union[float, None] = None
        self.cost: Union[int, None] = self.calculate_cost()

    def calculate_cost(self) -> Union[int, None]:
        current_node: "Node" = self.parent
        cost = 0
        while current_node is not None:
            cost += 1
            current_node = current_node.parent
        return cost
