"""
Function will place flag at the given cell
Input: x, y

Author:
D.R.K. DISANAYAKA - 21/ENG/022
"""

def place_flag(self,x,y):
    # check x and y within the grid
    if x < 0 or x >= self.size or y < 0 or y >= self.size:
        # throw exception
        raise Exception("Invalid cell")
    
    # check if already has flag
    if self.grid[x][y][1] == self.cell_status.CELL_STATUS_NOT_REVEALED:
        # reveal the cell
        self.grid[x][y][1] = self.cell_status.CELL_STATUS_FLAGGED
        print("\nFlag was placed\n")
    elif self.grid[x][y][1] == self.cell_status.CELL_STATUS_FLAGGED:
        # remove flag
        self.grid[x][y][1] = self.cell_status.CELL_STATUS_NOT_REVEALED
        print("\nFlag was removed\n")    
