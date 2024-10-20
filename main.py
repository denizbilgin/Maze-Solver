import sys
from StackFringe import StackFringe
from QueueFringe import QueueFringe
from PriorityQueueFringe import PriorityQueueFringe
from IterativeDeepeningStackFringe import IterativeDeepeningStackFringe
from Maze import Maze
import os


if __name__ == '__main__':
    fringe = PriorityQueueFringe("euclidean")
    maze = Maze("mazes/maze2.txt", fringe)

    print("Maze: ")
    maze.print_maze()
    print("Solving...")
    maze.solve()
    print("States Explored:", maze.num_explored)
    print("Solution:")
    maze.print_maze()
    maze.output_image(show_explored=True)
