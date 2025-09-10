import pygame, sys
from game import Game 
from mycolors import MyColors

pygame.init()

# Font & text surface
title_font= pygame.font.Font(None, 40)
score_surface= title_font.render("Score", True, MyColors.white)
next_surface= title_font.render("Next", True, MyColors.white)
game_over_surface= title_font.render("GAME OVER", True, MyColors.white)

# UI rectangles (score box and next-block preview box)
score_rect= pygame.Rect(320, 55, 170, 60)
next_rect= pygame.Rect(320, 215, 170, 180)

# Game window
screen= pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Clock controls FPS
clock= pygame.time.Clock()

# Initial game logic
game= Game()
# Custom event to control block drop speed
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)    # Every 300ms

# Main game loop

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close window
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: # Keyboard input
            if game.game_over == True:    # Restart game if over
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)    # +1 pt for soft drop
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            # Block automatically falls over time
            game.move_down()

    #Drawing
    score_value_surface = title_font.render(str(game.score), True, MyColors.white)

    # Bckground color
    screen.fill(MyColors.dark_blue)    

    # UI Labels
    screen.blit(score_surface, (365, 20, 50, 50)) 
    screen.blit(next_surface, (375, 180, 50, 50))

    # Game over text
    if game.game_over:
        screen.blit(game_over_surface, (320, 450))

    # Score box
    pygame.draw.rect(screen, MyColors.light_blue, score_rect, 0, 10)     
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx= score_rect.centerx,
        centery= score_rect.centery))

    # Next block preview box
    pygame.draw.rect(screen, MyColors.light_blue, next_rect, 0, 10)

    # Draw game grid+blocks
    game.draw(screen)   
  
    # Update display and tick clock
    pygame.display.update()
    # Cap frame rate at 60 FPS
    clock.tick(60)                   

    
