from collections import namedtuple
from random import choice

Coord = namedtuple("Coord", "x y")

EAST = "EAST"
WEST = "WEST"
NORTH = "NORTH"
SOUTH = "SOUTH"

class Maze():
    def __init__(self, width=10):
        if width < 10:
            print ("Width must be at least 10. Set to 10.")
            #width = 10
        self.maze_width = width
        self.maze = []
        self.complete_trace = []
        # init maze to all zeros
        for _ in range(self.maze_width):
            temp = []
            for _ in range(self.maze_width):
                temp.append(0)
            self.maze.append(temp)

        '''    TESTING GET_DIRECTIONS
            self.maze[0][0] = 1
            self.maze[0][1] = 1
            self.maze[1][1] = 1
            self.maze[2][1] = 1
            self.maze[2][2] = 1
            self.maze[3][2] = 1
            self.maze[4][2] = 1
        
                    Y
                *  0 1 2 3 4 
                0  1 1 0 0 0          W
                1  0 1 0 0 0       S <-> N
            X  2  0 1 1 0 0          E
                3  0 0 1 0 0
                4  0 0 1 0 0
            
            p = Coord(x=0, y=0)
            print(self.get_directions(p))
        '''
        # intit maze entry Coord (0,0) to 1
        self.maze[0][0] = 1
        # set Coorder for position to entry Coord
        pos_ptr = Coord(x=0,y=0)
        # intit trace with 
        trace = []
        # while trace contains directions to go
        while True:
            self.complete_trace.append(pos_ptr)
            directions = self.get_directions(pos_ptr)
            # CASE 1: directions not empty
            if directions:
                # get random direction from possible
                direction = choice(directions)
                # push direction onto trace stack
                trace.append(direction)
                # set pos_Coorder to next position
                pos_ptr = self.apply_direction(pos_ptr,direction)
                #self.complete_trace.append(pos_ptr)
                # mark next position
                self.maze[pos_ptr.x][pos_ptr.y] = 1
            # CASE 2: no available directions, backtrack!
            else:
                # get next direction from the reverse of the trace top
                next_dir = self.reverse_direction(trace.pop())
                # CASE 2a: trace = [ 'END' ] => EXIT
                if len(trace) == 0:
                    break
                # CASE 2b: trace = [ dir1, ... , 'END' ]
                else:
                    # move Coorder to backtracked position
                    pos_ptr = self.apply_direction(pos_ptr,next_dir)
                    #self.complete_trace.append(pos_ptr)

    def get_directions(self, pos):
        directions = []
        # IF next_pos(dir) in bounds && not backwards(dir)
        # Check (x+1,y) - EAST
        if (pos.x + 1 < self.maze_width and self.maze[pos.x+1][pos.y] != 1):
            east_pos = Coord(x=pos.x+1,y=pos.y)
            if self.valid_direction(east_pos, EAST):
                directions.append(EAST)

        # Check (x-1,y) - WEST
        if (pos.x - 1 >= 0 and self.maze[pos.x-1][pos.y] != 1):
            west_pos = Coord(x=pos.x-1,y=pos.y)
            if self.valid_direction(west_pos, WEST):
                directions.append(WEST)

        # Check (x,y+1) - NORTH
        if (pos.y + 1 < self.maze_width and self.maze[pos.x][pos.y+1] != 1):
            north_pos = Coord(x=pos.x,y=pos.y+1)
            if self.valid_direction(north_pos, NORTH):
                directions.append(NORTH)

        # Check (x,y-1) - SOUTH
        if (pos.y - 1 >= 0 and self.maze[pos.x][pos.y-1] != 1):
            south_pos = Coord(x=pos.x,y=pos.y-1)
            if self.valid_direction(south_pos, SOUTH):
                directions.append(SOUTH)
        return directions
    def valid_direction(self,pos,dir):
        ''' 
            for each direction:
                if ( COND_1 && COND_2 && COND_3 ):
                    return False  # direction/spot is invalid
                # COND_1  ->  ensure we're not checking the spot we came from
                # COND_2  ->  ensure we're not checking out of bounds 
                              (it's okay for us to be on the edge)
                # COND_3  ->  check if the spot is marked 
        '''
        # check EAST of position
        if dir != WEST and pos.x+1 < self.maze_width and self.maze[pos.x+1][pos.y] == 1:
            return False
        # check WEST of position
        if dir != EAST and pos.x-1 >= 0 and self.maze[pos.x-1][pos.y] == 1:
            return False
        # check NORTH of position
        if dir != SOUTH and pos.y+1 < self.maze_width and self.maze[pos.x][pos.y+1] == 1:
            return False
        # check SOUTH of position
        if dir != NORTH and pos.y-1 >= 0 and self.maze[pos.x][pos.y-1] == 1:
            return False
        # if passed all 4 checks, valid direction/spot, return True
        return True
    def apply_direction(self,pos,dir):
        if dir == EAST:
            return Coord(x = pos.x+1, y = pos.y)
        elif dir == WEST:
            return Coord(x = pos.x-1, y = pos.y)
        elif dir == NORTH:
            return Coord(x = pos.x, y = pos.y+1)
        elif dir == SOUTH:
            return Coord(x = pos.x, y = pos.y-1)
        else:
            print ("Error: apply_direction() -> invalid direction arg: ", dir)
    def reverse_direction(self, dir):
        if dir == NORTH:
            return SOUTH
        elif dir == SOUTH:
            return NORTH
        elif dir == WEST:
            return EAST
        elif dir == EAST:
            return WEST
        else:
            print("Error: reverse_direction() -> invalid direction arg: ", dir)
    def print_maze(self):
        # print compass
        print ('   W')
        print ('S <=> N')
        print ('   E')
        print ('X  ',end='')
        for i in range(self.maze_width):
            print(i,end='  ')
        print()
        for r in range(self.maze_width):
            print(r,end='  ')
            for c in range(self.maze_width):
                print(self.maze[r][c],' ',end='')
            print()
