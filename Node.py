class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = None

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __gt__(self, other):
        return self.heuristic > other.heuristic
