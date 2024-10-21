import sys
from AStarPriorityQueueFringe import AStarPriorityQueueFringe
from StackFringe import StackFringe
from QueueFringe import QueueFringe
from PriorityQueueFringe import PriorityQueueFringe
from IterativeDeepeningStackFringe import IterativeDeepeningStackFringe
from UniformCostPriorityQueueFringe import UniformCostPriorityQueueFringe
from BeamPriorityQueueFringe import BeamPriorityQueueFringe
from Maze import Maze
import os


if __name__ == '__main__':
    fringe = BeamPriorityQueueFringe()
    maze = Maze("mazes/maze3.txt", fringe)

    print("Maze: ")
    maze.print_maze()
    print("Solving...")
    maze.solve()
    print("States Explored:", maze.num_explored)
    print("Solution:")
    maze.print_maze()
    maze.output_image(show_explored=True)
