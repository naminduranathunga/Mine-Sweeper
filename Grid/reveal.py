"""
Function will check & reveal the given cell
Input: x, y
Output: True/False

Author:
R.A.N.S Ranathunga - 21/ENG/107
"""

def reveal(self, x, y):
    # check x and y within the grid
    if x < 0 or x >= self.size or y < 0 or y >= self.size:
        # throw exception
        raise Exception("Invalid cell")
    
    # check if the cell is already revealed
    if self.grid[x][y][1] != self.cell_status.CELL_STATUS_REVEALED:
        # reveal the cell
        self.grid[x][y][1] = self.cell_status.CELL_STATUS_REVEALED
    
    # check whether it is a mine
    return not (self.grid[x][y][0] == -1)
    #if self.grid[x][y][0] == -1: # mine
    #    return False # game over
    #else:
    #    return True