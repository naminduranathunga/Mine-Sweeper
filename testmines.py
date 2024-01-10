"""
Test Place mines
"""
import Grid


cg = Grid.Grid(6,3)
cg.place_mines()
cg.calculate_cell_value()
for i in range(6):
    for j in range(6):
        cg.reveal(i, j)
cg.print_grid()

