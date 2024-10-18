import sys
from StackFringe import StackFringe
from QueueFringe import QueueFringe
from Maze import Maze


if __name__ == '__main__':
    USE_COMMAND_LINE = False
    if USE_COMMAND_LINE:
        if len(sys.argv) != 2:
            sys.exit("Usage: python maze.py maze.txt")
        maze = Maze(sys.argv[1], QueueFringe)
    else:
        maze_path = "maze3.txt"
        maze = Maze(maze_path, QueueFringe)

    print("Maze: ")
    maze.print_maze()
    print("Solving...")
    maze.solve()
    print("States Explored:", maze.num_explored)
    print("Solution:")
    maze.print_maze()
    maze.output_image("mazeQueue.png", show_explored=True)
