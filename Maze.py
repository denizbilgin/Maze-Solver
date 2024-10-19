from typing import Tuple, List, Union, Type
from Node import Node
from PIL import Image, ImageDraw
from Fringe import Fringe
from HeuristicFringe import HeuristicFringe


class Maze:
    def __init__(self, filename: str, fringe: Type[Fringe]) -> None:
        self.filename: str = filename
        # Reading given maze
        self.__perceive_maze(self.filename)
        self.solution: Union[Tuple[List, List], None] = None
        self.num_explored: int = 0
        self.explored: Union[set, None] = None
        self.fringe = fringe()

    def __perceive_maze(self, filename: str) -> None:
        if ".txt" not in filename:
            raise TypeError("Type of the maze must be a text file (txt).")

        with open(filename) as f:
            contents: str = f.read()

        # Validating start and goal
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point.")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal.")

        contents: list[str] = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keeping track of walls and some important states
        self.walls: list[list[bool]] = []
        for i in range(self.height):
            row: list[bool] = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start_state = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal_state = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

    def print_maze(self) -> None:
        solution: Union[List, None] = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start_state:
                    print("A", end="")
                elif (i, j) == self.goal_state:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state: Tuple[int, int]) -> List[Tuple[str, Tuple[int, int]]]:
        row, col = state
        candidates: List[Tuple[str, Tuple[int, int]]] = [
            ("up",    (row - 1, col)),
            ("down",  (row + 1, col)),
            ("left",  (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result: List[Tuple[str, Tuple[int, int]]] = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self, distance_type: str = "manhattan") -> None:
        """
        Finds a solution to maze, if one exists.
        :return: None
        """
        # Keeping track of number of states explored
        self.num_explored = 0

        # Initializing the fringe
        start = Node(self.start_state, None, None)
        if isinstance(self.fringe, HeuristicFringe):
            self.fringe.goal_state = self.goal_state
            self.fringe.set_distance_type(distance_type)
        self.fringe.add(start)

        # Initializing an empty explored set
        self.explored = set()

        # Looping until solution found
        while True:
            if self.fringe.is_empty():
                raise Exception("No solution. Fringe is empty.")

            # Choose a node from the fringe
            node = self.fringe.remove()

            self.num_explored += 1

            if node.state == self.goal_state:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Marking node as explored
            self.explored.add(node.state)

            # Adding neighbors to fringe
            for action, state in self.neighbors(node.state):
                if not self.fringe.contains_state(state) and state not in self.explored:
                    child = Node(state, node, action)
                    self.fringe.add(child)

    def output_image(self, show_solution: bool = True, show_explored: bool = False):
        filename = "solutions/" + self.filename[6:11] + self.fringe.__class__.__name__ + "_" + str(self.num_explored) + ".png"

        cell_size: int = 50
        cell_border: int = 2

        # Creating a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                if col:                           # Walls
                    fill = (40, 40, 40)
                elif (i, j) == self.start_state:  # Start
                    fill = (255, 0, 0)
                elif (i, j) == self.goal_state:   # Goal
                    fill = (0, 171, 28)
                elif solution is not None and show_solution and (i, j) in solution:         # Solution
                    fill = (220, 235, 113)
                elif solution is not None and show_explored and (i, j) in self.explored:    # Explored
                    fill = (212, 97, 85)
                else:                                                                       # Empty Cell
                    fill = (237, 240, 252)

                # Drawing cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
        img.save(filename)
