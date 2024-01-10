"""
This function will print grid in a tabular format
F - Flagged
. - No mines around
1-8 - Number of mines around

"""

import tabulate

def print_grid(self):
    #self.grid = [[0 for x in range(10)] for y in range(10)]
    # Add extra raw and extra column to the grid
    # to print the numbers and letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    pg_size = self.size + 1
    print_grid = [[" " for x in range(pg_size)] for y in range(pg_size)]
    print_grid[0][0] = " "
    for x in range(1, pg_size):
        print_grid[0][x] = letters[x]
        print_grid[x][0] = letters[x]


    # fill the grid with the numbers and letters
    for x in range(1, pg_size):
        for y in range(1, pg_size):
            # if cell is revealed
            if (self.grid[x-1][y-1][1] == self.cell_status.CELL_STATUS_REVEALED):
                if (self.grid[x-1][y-1][0] == -1):
                    print_grid[x][y] = "M"
                elif (self.grid[x-1][y-1][0] == 0):
                    print_grid[x][y] = "." # no mines around
                else:
                    print_grid[x][y] = str(self.grid[x-1][y-1][0])
            elif (self.grid[x-1][y-1][1] == self.cell_status.CELL_STATUS_FLAGGED):
                print_grid[x][y] = "F"

    print(tabulate.tabulate(print_grid, tablefmt="grid"))