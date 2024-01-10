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
    
    return self.reveal_cells_recursive(x, y)
    
   