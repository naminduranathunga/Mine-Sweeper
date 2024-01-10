class Grid:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.revealed_cells = 0
        self.max_cells = 0
        self.grid = [[[0,0]for _ in range(size)]for _ in range(size)]

        pass

    from .print_grid import print_grid



    # for Namindu


    ##############################

    from .place_mines import place_mines
    

