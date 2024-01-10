def calculate_cell_value(self):

    for x in range(self.size):
        for y in range(self.size):
            if self.grid[x][y][0] != -1:
                count = 0
                for i in range(max(0, x - 1), min(self.size, x + 2)):
                    for j in range(max(0, y - 1), min(self.size, y + 2)):
                        if self.grid[i][j][0] == -1:
                            count += 1
                self.grid[x][y] = (count, self.grid[x][y][1])