import pygame
from mycolors import MyColors

class Grid:

    def __init__(self):
        """ Initialize the game grid with empty cells."""
        self.num_rows= 20    # Standard Tetris height
        self.num_cols= 10    # Standard Tetris width
        self.cell_size= 30   #  Size of each cell in pixels
        # 2D array storing block IDs (0 = empty)
        self.grid= [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # Color lookup for each block ID
        self.colors= MyColors.get_cell_colors()

    def print_grid(self):
        """ Print the grid values in the console"""
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end= " ")
            print()    

    def is_inside(self, row, column):
        """ Check if a cell is within grid boundaries"""
        if row >=0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):
        """ Check if a given cell is empty (contains 0)"""
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        """ Check if a row is completely filled with non-zero values"""
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
        
    def clear_row(self, row):
        """ Clear a given row (set all its cells to 0)"""
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """ 
        Move a row down by 'num_rows'
        Useful when rows above a cleared line must drop down.
        """
        for comun in range(self.num_cols):
            self.grid[row+num_rows][column]= self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        clear all full rows in the grid.
        Reruns: completed(init): number of rows cleared
        """
        completed = 0
        # Start from bottom row and move upward
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed >0:
                # Drop down rows above cleared lines
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        """ Reset the grid (set all cells to empty) """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column]= 0

  
    def draw(self, screen):
        """ Draw the grid cells on the screen """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Create a rect with slight spacing (-1) for visible lines
                cell_rect= pygame.Rect(column* self.cell_size +11, row*self.cell_size +11, 
                self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
