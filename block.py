from mycolors import MyColors
from position import Position
import pygame

class Block:

    def __init__(self, id):
        # Unique identifier for the block/ used for color selection
        self.id= id
        self.cells= {}
        self.row_offset= 0
        self.column_offset= 0
        self.rotation_state= 0
        self.cell_size= 30
        self.rotation_state= 0
        self.colors= MyColors.get_cell_colors()

    def move(self, rows, columns):
        # Move the block by adjusting its row and column offsets.
        # Rows: how many rows to move(positive= down, negative= up)
        # Columns: how many columns to move(positive= right, negative= left)
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_position(self):
        # Return the absolute positions of the block tiles on the grid
        tiles = self.cells[self.rotation_state]
        moved_tiles= []
        for pos in tiles:
            moved_tiles.append(Position(pos.row +self.row_offset, pos.column + self.column_offset))

        return moved_tiles
    
    def rotate(self):
        # Rotate the block clockwise to the next rotation state.
        # Wraps around when reaching the last state
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        # Revert the last rotation to avoid collition(counter-clokwise)
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) -1

    def draw(self, screen, offset_x= 0, offset_y= 0):
        # Draw the block on the given pygame screen
        # offset_x, offset_y: extra pixel offsets to position the board on screen
        tiles= self.get_cell_position()
        for tile in tiles:
            tile_rect= pygame.Rect(offset_x + tile.column*self.cell_size, 
                offset_y + tile.row*self.cell_size,
                    self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
