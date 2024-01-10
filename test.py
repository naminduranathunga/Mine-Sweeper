"""
Test Print grid
"""
import Grid

import random

cg = Grid.Grid(4, 4)
cg.grid[1][1] = [-1,0]
cg.grid[1][2] = [1,0]
cg.grid[2][2] = [1,0]
cg.print_grid()

print("Revealing...")
cg.reveal(0,0)
cg.print_grid()

