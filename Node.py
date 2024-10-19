class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = None

    def __lt__(self, other):
        if self.heuristic is not None and other.heuristic is not None:
            return self.heuristic < other.heuristic
        else:
            raise ValueError("Heuristic of this node is None. You need to set it for comparing nodes.")

    def __gt__(self, other):
        if self.heuristic is not None and other.heuristic is not None:
            return self.heuristic > other.heuristic
        else:
            raise ValueError("Heuristic of this node is None. You need to set it for comparing nodes.")
