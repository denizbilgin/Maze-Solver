# Maze Solver

This repository contains implementations of several **maze-solving algorithms**, adhering to the principles of **clean code** and **class-based architecture**. Each algorithm is designed to solve various maze problems efficiently, making the code easy to read, maintain, and extend. The codebase demonstrates the use of well-defined classes, modular functions, and encapsulation, ensuring that the algorithms are both reusable and adaptable.

The implemented algorithms include classic and modern maze-solving techniques:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **A-Star Search**
- **Beam Search**
- **Greedy Best-First Search**
- **Iterative Deepening Search**
- **Uniform Cost Search (UCS)**

In the `solutions` folder, you can find PNG files that visually represent the solutions of four different mazes using each implemented algorithm. These images provide a clear illustration of how each algorithm navigates through the mazes.

You can test these algorithms with your own created mazes and get a clearer idea of ​​how they work. In the `mazes` folder you can find a total of 4 mazes that measure different things that I use to test the algorithms. You can also create your own maze as a txt file. The `__perceive_maze()` function in the `maze.py` file sets some rules to detect the maze you created.
- There should be only one starting point in a maze and that point should be indicated with the symbol `A`.
- There should be only one ending (target) point in a maze and that point should be indicated with the symbol `B`.
- Walls are marked with `#` signs.
- The " ", that is, the empty spaces, represent the paths that can be followed.
Then you need to put your own maze file to `mazes` folder. Finally, you can run it!

## How to Run the Code

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/denizbilgin/Maze-Solver.git
2. Select algorithm and maze in `main.py` file:
   ```bash
   fringe = UniformCostSearch()
   maze = Maze("mazes/maze4.txt", fringe)

<br>

## Maze 2 Solutions

<table>
  <tr>
    <td><b>Depth-First Search (DFS)</b> 194 steps</td>
    <td><b>Breadth-First Search (BFS)</b> 77 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_DepthFirstSearch_194.png" alt="DFS Solution for Maze 2" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_BreadthFirstSearch_77.png" alt="BFS Solution for Maze 2" width="400"></td>
  </tr>
  <tr>
    <td><b>A* Search</b> 59 steps</td>
    <td><b>Beam Search</b> 49 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_AStarSearch_59.png" alt="A* Search Solution for Maze 2" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_BeamSearch_49.png" alt="Beam Search Solution for Maze 2" width="400"></td>
  </tr>
  <tr>
    <td><b>Greedy Best-First Search</b> 54 steps</td>
    <td><b>Iterative Deepening Search</b> 69 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_GreedyBestFirstSearch_54.png" alt="Greedy BFS Solution for Maze 2" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_IterativeDeepeningSearch_69.png" alt="Iterative Deepening Search Solution for Maze 2" width="400"></td>
  </tr>
  <tr>
    <td><b>Uniform Cost Search (UCS)</b> 77 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze2_UniformCostSearch_77.png" alt="Uniform Cost Search Solution for Maze 2" width="400"></td>
  </tr>
</table>

<br><br>

## Maze 3 Solutions

<table>
  <tr>
    <td><b>Depth-First Search (DFS)</b> 17 steps</td>
    <td><b>Breadth-First Search (BFS)</b> 6 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_DepthFirstSearch_17.png" alt="DFS Solution for Maze 3" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_BreadthFirstSearch_6.png" alt="BFS Solution for Maze 3" width="400"></td>
  </tr>
  <tr>
    <td><b>A* Search</b> 5 steps</td>
    <td><b>Beam Search</b> 5 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_AStarSearch_5.png" alt="A* Search Solution for Maze 3" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_BeamSearch_5.png" alt="Beam Search Solution for Maze 3" width="400"></td>
  </tr>
  <tr>
    <td><b>Greedy Best-First Search</b> 5 steps</td>
    <td><b>Iterative Deepening Search</b> 8 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_GreedyBestFirstSearch_5.png" alt="Greedy BFS Solution for Maze 3" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_IterativeDeepeningSearch_8.png" alt="Iterative Deepening Search Solution for Maze 3" width="400"></td>
  </tr>
  <tr>
    <td><b>Uniform Cost Search (UCS)</b> 6 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze3_UniformCostSearch_6.png" alt="Uniform Cost Search Solution for Maze 3" width="400"></td>
  </tr>
</table>

<br><br>

## Maze 4 Solutions

<table>
  <tr>
    <td><b>Depth-First Search (DFS)</b> 285 steps</td>
    <td><b>Breadth-First Search (BFS)</b> 386 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_DepthFirstSearch_285.png" alt="DFS Solution for Maze 4" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_BreadthFirstSearch_386.png" alt="BFS Solution for Maze 4" width="400"></td>
  </tr>
  <tr>
    <td><b>A* Search</b> 261 steps</td>
    <td><b>Beam Search</b> 125 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_AStarSearch_261.png" alt="A* Search Solution for Maze 4" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_BeamSearch_125.png" alt="Beam Search Solution for Maze 4" width="400"></td>
  </tr>
  <tr>
    <td><b>Greedy Best-First Search</b> 103 steps</td>
    <td><b>Iterative Deepening Search</b> 261 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_GreedyBestFirstSearch_103.png" alt="Greedy BFS Solution for Maze 4" width="400"></td>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_IterativeDeepeningSearch_261.png" alt="Iterative Deepening Search Solution for Maze 4" width="400"></td>
  </tr>
  <tr>
    <td><b>Uniform Cost Search (UCS)</b> 386 steps</td>
  </tr>
  <tr>
    <td><img src="https://github.com/denizbilgin/Maze-Solver/blob/main/solutions/maze4_UniformCostSearch_386.png" alt="Uniform Cost Search Solution for Maze 4" width="400"></td>
  </tr>
</table>
