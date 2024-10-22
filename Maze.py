from typing import Tuple, List, Union
from Node import Node
from PIL import Image, ImageDraw
from Fringe import Fringe
from HeuristicFringe import HeuristicFringe


class Maze:
    """
    Represents a maze for pathfinding, with capabilities to load a maze from a file,
    solve it using a given search algorithm, and output the solution visually.
    """
    def __init__(self, filename: str, fringe: Fringe) -> None:
        self.filename: str = filename
        # Reading given maze
        self.__perceive_maze(self.filename)     # Sets self.height, self.width, self.walls, self.start_state, self.goal_state
        self.solution: Union[Tuple[List, List], None] = None
        self.num_explored: int = 0
        self.explored: Union[set, None] = None
        self.fringe = fringe

    def __perceive_maze(self, filename: str) -> None:
        """
        Reads the maze structure from the specified file and initializes the maze attributes.

        The maze file should contain exactly one start point ("A") and one goal point ("B").
        Walls are represented by any character other than spaces (" "), "A", or "B".
        :param filename: The name of the maze file to load.
        :return: None
        """
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
        """
        Prints the current maze to the console, showing the start point (A), goal point (B),
        walls, and solution path if it has been found.
        :return: None
        """
        solution: Union[List[Tuple[int, int]], None] = self.solution[1] if self.solution is not None else None

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
        """
        Returns the valid neighboring states for a given state.

        The neighboring states are those that are within the bounds of the maze and are not walls.
        :param state: The current state in the maze (x, y).
        :return: A list of tuples where the first element is the action (e.g., "up", "down")
            and the second element is the neighboring state.
        """
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

    def solve(self) -> None:
        """
        Solves the maze using the specified search algorithm.

        The algorithm continues until a solution is found or all possible states are explored.
        If a solution is found, the sequence of actions and cells leading to the goal is stored.
        :return: None
        """
        # Keeping track of number of states explored
        self.num_explored = 0

        # Initializing the fringe
        start = Node(self.start_state, None, None)
        if isinstance(self.fringe, HeuristicFringe):
            self.fringe.goal_state = self.goal_state
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
                actions: list[str] = []
                cells: list[Tuple[int, int]] = []
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

    def output_image(self, show_solution: bool = True, show_explored: bool = False) -> None:
        """
        Outputs an image of the maze, showing the start, goal, solution path, and optionally the explored nodes.

        The image is saved as a PNG file in the "solutions" directory.
        :param show_solution: If True, the solution path will be displayed in the image (default is True).
        :param show_explored: If True, the explored nodes will be displayed in the image (default is False).
        :return: None
        """
        filename = "solutions/" + self.filename[6:11] + "_" + self.fringe.__class__.__name__ + "_" + str(self.num_explored) + ".png"

        cell_size: int = 50
        cell_border: int = 2

        # Creating a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution: Union[List[Tuple[int, int]], None] = self.solution[1] if self.solution is not None else None
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
