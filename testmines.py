"""
Test Place mines
"""
import Grid


cg = Grid.Grid(7,8)
cg.place_mines()
cg.calculate_cell_value()
for i in range(7):
    for j in range(7):
        cg.reveal(i, j)
cg.print_grid()

