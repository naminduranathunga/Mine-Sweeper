"""
Test Print grid
"""
import Grid

import random

cg = Grid.Grid(4, 1)
cg.grid[1][1] = [-1,0]
cg.grid[1][2] = [1,0]
cg.grid[2][2] = [1,0]
cg.calculate_cell_value()
cg.print_grid()

print("Revealing...")
cg.reveal(0,0)
#if (not cg.reveal(1,1)):
#    print("Game Over")
if (cg.max_cells == cg.revealed_cells):
    print("You Won")
else:
    print(cg.revealed_cells, cg.max_cells)
cg.print_grid()

print("")

cg.reveal(3,3)
#if (not cg.reveal(1,1)):
#    print("Game Over")
if (cg.max_cells == cg.revealed_cells):
    print("You Won")
else:
    print(cg.revealed_cells, cg.max_cells)
cg.print_grid()

