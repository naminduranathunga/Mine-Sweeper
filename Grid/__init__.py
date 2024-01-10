class Grid:
    def __init__(self, size, num_mines, status, revealed_cells, max_cells):
        self.size = size
        self.num_mines = num_mines
        self.status = status
        self.revealed_cells = revealed_cells
        self.max_cells = max_cells
        self.grid = [[[0,0]for _ in range(size)]for _ in range(size)]

        pass

    from .print_grid import print_grid



    # for Namindu


    ##############################


    

