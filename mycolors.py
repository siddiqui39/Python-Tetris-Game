class MyColors:
    
    """
    Defines color constants (RGB tuples) used throughout the Tetris game.
    Provides a helper method to map block IDs to their colors
    """
    dark_grey = (26, 31, 40)
    green= (47, 230, 23)
    red= (232, 18, 18)
    orange= (226, 116, 17)
    yellow= (237, 234, 4)
    purple= (166, 0, 247)
    cyan= (21, 204, 209)
    blue= (13, 64, 216)
    white= (255, 255, 255)
    dark_blue= (44,44,127)
    light_blue= (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
    """
    Return a list of block colors indexed by block ID.
    Index 0 = background (dark grey)
    IDs 1-7 = different Tetrominoes.
    """
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
