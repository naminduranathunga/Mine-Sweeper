"""
Function will place mines

Author:
W.A.H.K.Weerasinghe - 21/ENG/159
"""
import random
def place_mines(self):

    size = self.size

    i = 0
    while i < self.num_mines:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)

        if self.grid[x][y][0] == -1:
            continue
        else:
            self.grid[x][y][0] = -1

        i += 1





