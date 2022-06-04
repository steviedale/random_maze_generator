'''
    author: Steven Dale
    Project: aMAZEing
'''
from maze import Maze
from graphics import BoardDisplay, RED, GREEN
from time import sleep

maze_width = 20
path_width = 25

disp = BoardDisplay(num_rows=maze_width, num_columns=maze_width, width=path_width)
maze = Maze(maze_width)
disp.start(maze.complete_trace)
