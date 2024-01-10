"""
comments
"""
class Grid:
    def __init(self, size, num_mines, status, revealed_cells, max_cells):
        self.size = size
        self.num_mines = num_mines
        self.status = status
        self.revealed_cells = revealed_cells
        self.max_cells = max_cells
        self.grid = [[[0,0]for _ in range(size)]for _ in range(size)]

        pass

    def place_mines(self):
        pass

    def place_numbers(self):
        pass

    def print_grid(self):
        pass
    
    def reveal(self, x, y):
        pass

    def place_flag(self, x, y):
        pass

