import sys
from Fringe import Fringe
from StackFringe import StackFringe
from QueueFringe import QueueFringe
from PriorityQueueFringe import PriorityQueueFringe
from Maze import Maze
import os


def is_pycharm():
    # PyCharm, pydevd modülünü kullanır
    return 'PYCHARM_HOSTED' in os.environ or 'pydevd' in sys.modules


if __name__ == '__main__':
    if is_pycharm():
        fringe = PriorityQueueFringe
        maze = Maze("maze2.txt", fringe)
    elif len(sys.argv) > 1:
        fringes = {"StackFringe": StackFringe, "QueueFringe": QueueFringe, "PriorityQueueFringe": PriorityQueueFringe}
        if len(sys.argv) != 3:
            sys.exit("Usage: python maze.py maze.txt StackFringe")
        fringe = fringes[sys.argv[2]]
        maze = Maze(sys.argv[1], fringe)
        print(maze.filename)
    else:
        raise Exception("You need to run this file by command line or PyCharm.")

    print("Maze: ")
    maze.print_maze()
    print("Solving...")
    maze.solve()
    print("States Explored:", maze.num_explored)
    print("Solution:")
    maze.print_maze()
    maze.output_image(f"{maze.filename.replace(".txt", "").replace("\\", "")}{fringe.__name__}.png", show_explored=True)
