"""
This function will recursively reveal the cells around the given cell
Input: x, y
Output: True/False

Author:
R.A.N.S Ranathunga - 21/ENG/107
"""
def reveal_cells_recursive(self, x, y):
    # reveal the cell
    if self.grid[x][y][1] != self.cell_status.CELL_STATUS_REVEALED:
        self.grid[x][y][1] = self.cell_status.CELL_STATUS_REVEALED
        self.revealed_cells += 1
        if self.grid[x][y][0] == -1: # mine
            return False

    # for each cell around the given cell
    # if cell is not revealed and not flagged and not a mine then reveal it.
    # if any of it's value is 0 then call this function again for that cell
        for i in range(max(0, x-1), min(self.size, x+2)):
            for j in range(max(0, y-1), min(self.size, y+2)):
                # escape current cell
                if (i == x and j == y):
                    continue
                # reveal the cell if it is not revealed
                if self.grid[i][j][1] == self.cell_status.CELL_STATUS_NOT_REVEALED:
                    if self.grid[i][j][0] == 0:
                        self.reveal_cells_recursive(i, j)
                    elif self.grid[i][j][0] == -1:
                        continue
                    else:
                        self.grid[i][j][1] = self.cell_status.CELL_STATUS_REVEALED
                        self.revealed_cells += 1