import tabulate

def print_grid(self):
    self.grid = [[0 for x in range(10)] for y in range(10)]
    # Add extra raw and extra column to the grid
    # to print the numbers and letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    print_grid = [[" " for x in range(11)] for y in range(11)]
    print_grid[0][0] = " "
    for x in range(1, 11):
        print_grid[0][x] = letters[x]
        print_grid[x][0] = letters[x]

    # fill the grid with the numbers and letters
    for x in range(1, 11):
        for y in range(1, 11):
            print_grid[x][y] = self.grid[x-1][y-1]

    print("Printing grid...")

    print(tabulate.tabulate(print_grid, tablefmt="grid"))