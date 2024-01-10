"""
Test Print grid
"""
import Grid


cg = Grid.Grid(4, 4, 0,0,0)
cg.grid[1][1] = [-1,1]
cg.grid[1][2] = [1,1]
cg.grid[2][2] = [1,2]
cg.reveal(0,0)
cg.print_grid()

