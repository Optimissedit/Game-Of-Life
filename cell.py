import pygame as pg

RED = (255, 20, 20)


class Cell():
    # Constructor
    def __init__(self, left, top, size):

        self.x = left
        self.y = top
        self.size = size

    # returns a list of all possible neighboring cells
    def get_neighbors(self):
        return [Cell(self.x + 4, self.y, 4), Cell(self.x - 4, self.y, 4), Cell(self.x + 4, self.y + 4, 4),
                Cell(self.x + 4, self.y - 4, 4), Cell(self.x - 4, self.y + 4, 4), Cell(self.x - 4, self.y - 4, 4),
                Cell(self.x, self.y + 4, 4), Cell(self.x, self.y - 4, 4)]

    # Counts all the neighbor cells that exist in the world
    def counter(self, world_cells):
        # Grabs list of neighbors around this cell
        neighbors = self.get_neighbors()
        count = 0

        # Iterates through all neighbors, checking to see if they are in live set of cells
        for neighbor in neighbors:
            for cell in world_cells:
                if neighbor.x == cell.x and neighbor.y == cell.y:
                    # If neighboring cell is live, increment count
                    count += 1

        return count

    # Defines how cell should be printed as string
    def __str__(self):
        x = str(self.x)
        y = str(self.y)
        siz = str(self.size)
        return "Cell with position (" + x + ", " + y + "), of size " + siz + "."
