from all_blocks import *
from grid import Grid
import random
import pygame

class Game:
    def __init__(self):
        # Initialize the Tetris game state, sounds and background music
        print("Game initialized")
        self.grid= Grid()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score= 0
        self.rotate_sound= pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound= pygame.mixer.Sound("sounds/clear.ogg")

        pygame.mixer.music.load("sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        """ 
        Update the score based on cleared lines and soft drop points.
        1 line= 100 pts,
        2 lines= 300 pts,
        3 lines= 500 pts
        """
        if lines_cleared ==1:
            self.score += 100
        elif lines_cleared ==2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
        

    def get_random_block(self):
        """
        Return a random block from the pool.
        Ensure all 7 blocks are used before repeating
        """
        if len(self.blocks) == 0:
            # Refill with all 7 Tetrominoes
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block= random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        """ Move the current block one column left (if valid)"""
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        """ Move the current block one column right (if valid)"""
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        """
        Move the current block one row down.
        If it cannot move further, lock it in place
        """
        self.current_block.move(1, 0)
        if self.block_inside()== False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        """ 
        Place the current block permanently on the grid.
        Then spwn the next block and clear full rows
        """
        
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.column]= self.current_block.id
        # Swap in next block
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        # Clear completed rows
        rows_cleared =self.grid.clear_full_rows()
        if rows_cleared >0:
            self.clear_sound.play()
        self.update_score(rows_cleared, 0)
        # Check if new block fits (otherwise game over) 
        if self.block_fits() == False:
            self.game_over = True

    def  reset(self):
        """ Restart the game with a fresh grid and score"""
        self.grid.reset()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score= 0

    def block_fits(self):
        """ Check if the current block fits in its current position"""
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True


    def rotate(self):
        """ 
        Rotate the current block clockwise.
        Undo rotation if it does not fit
        """
        
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        """ Check if the current block is fully inside the grid boundaries"""
        tiles= self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
        """ Draw the grid, current block and preview of the next block"""
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11) # Current block

        # Positioning the preview of the next black depends on shape
        if self.next_block.id == 3:    # I-block
            self.next_block.draw(screen, 225, 290)
        elif self.next_block.id ==4 :    # O-block
            self.next_block.draw(screen, 255, 280)
        else:                             # Other blocks
            self.next_block.draw(screen, 270, 270)



