from typing import Tuple, Union


class Node:
    """
    Represents a node in a search tree, typically used in search algorithms like A* or BFS.

    Each node contains a state, a reference to its parent node, the action that led to it,
    and additional attributes such as the heuristic value and the path cost from the root node.
    """
    def __init__(self, state: Tuple[int, int], parent: Union["Node", None], action: Union[str, None]):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic: Union[float, None] = None
        self.cost: Union[int, None] = self.calculate_cost()

    def calculate_cost(self) -> Union[int, None]:
        """
        Calculates the total path cost from the root node to the current node.

        The cost is calculated by traversing the chain of parent nodes, counting
        the number of steps it takes to reach the root node. If the node is the root,
        the cost will be 0.
        :return: The total path cost from the root node to this node. Returns 0 if this node is the root.
        """
        current_node: "Node" = self.parent
        cost = 0
        while current_node is not None:
            cost += 1
            current_node = current_node.parent
        return cost
