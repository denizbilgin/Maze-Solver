from AStarSearch import AStarSearch
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from GreedyBestFirstSearch import GreedyBestFirstSearch
from IterativeDeepeningSearch import IterativeDeepeningSearch
from UniformCostSearch import UniformCostSearch
from BeamSearch import BeamSearch
from HandSearch import HandSearch
from Maze import Maze


if __name__ == '__main__':
    fringe = HandSearch(False)
    maze = Maze("mazes/maze1.txt", fringe)

    print("Maze: ")
    maze.print_maze()
    print("Solving...")
    maze.solve()
    print("States Explored:", maze.num_explored)
    print("Solution:")
    maze.print_maze()
    maze.output_image(show_explored=True)
