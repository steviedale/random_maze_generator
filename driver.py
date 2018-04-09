'''
    author: Steven Dale
    Project: aMAZEing
'''
from Maze import Maze
from graphics import *
from time import sleep

maze_width = 20
path_width = 25

win = GraphWin("aMAZEing",maze_width*path_width, maze_width*path_width)
maze = Maze(maze_width)

def draw_square(pt, color):
    pt1 = Point(pt.x*path_width, pt.y*path_width)
    pt2 = Point((pt.x + 1) * path_width, (pt.y + 1) * path_width)
    square = Rectangle(pt1,pt2)
    square.setFill(color)
    square.draw(win)

outer_border = Rectangle(Point(0,0),Point(maze_width*path_width,maze_width*path_width))
outer_border.draw(win)

for p in maze.complete_trace:
    pt = Point(p.x,p.y)
    sleep(0.05)
    draw_square(pt,'black')
    sleep(0.05)
    draw_square(pt,'red')

input() 