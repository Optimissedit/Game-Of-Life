import pygame as pg

RED = (255, 20, 20)


class Cell():
    def __init__(self, left, top, size):

        self.x = left
        self.y = top
        self.size = size

    def get_neighbors(self):
        return [Cell(self.x + 4, self.y, 4), Cell(self.x - 4, self.y, 4), Cell(self.x + 4, self.y + 4, 4),
                Cell(self.x + 4, self.y - 4, 4), Cell(self.x - 4, self.y + 4, 4), Cell(self.x - 4, self.y - 4, 4),
                Cell(self.x, self.y + 4, 4), Cell(self.x, self.y - 4, 4)]

    def __str__(self):
        x = str(self.x)
        y = str(self.y)
        siz = str(self.size)
        return "Cell with position (" + x + ", " + y + "), of size " + siz + "."
