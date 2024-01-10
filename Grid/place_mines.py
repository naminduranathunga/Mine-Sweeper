import random
def place_mines(self, size):
    x = 0

    while x < self.num_mines:
        x = random.randint(0, size)
        y = random.randint(0, size)

        if self.grid[x][y][0] == -1:
            continue
        else:
            self.grid[x][y][0] = -1

        x += 1




