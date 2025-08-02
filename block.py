from mycolors import MyColors
from position import Position
import pygame

class Block:

    def __init__(self, id):
        self.id= id
        self.cells= {}
        self.row_offset= 0
        self.column_offset= 0
        self.rotation_state= 0
        self.cell_size= 30
        self.rotation_state= 0
        self.colors= MyColors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles= []
        for pos in tiles:
            moved_tiles.append(Position(pos.row +self.row_offset, pos.column + self.column_offset))

        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) -1

    def draw(self, screen, offset_x= 0, offset_y= 0):
        tiles= self.get_cell_position()
        for tile in tiles:
            tile_rect= pygame.Rect(offset_x + tile.column*self.cell_size, 
                offset_y + tile.row*self.cell_size,
                    self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
