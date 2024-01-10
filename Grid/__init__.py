class Grid:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.revealed_cells = 0
        self.max_cells = (size * size) - num_mines
         # [<num_mines>, <status>] - 0: not revealed, 1: revealed, 2: flagged
        self.grid = [[[0,0]for _ in range(size)]for _ in range(size)]

        pass

    from .print_grid import print_grid


    # for Namindu
    from .reveal import reveal
    from .cell_status_const import cell_status
    from .reveal_cells_recursive import reveal_cells_recursive
    ##############################

    from .place_mines import place_mines
    from .calculate_cell_value import calculate_cell_value
    

