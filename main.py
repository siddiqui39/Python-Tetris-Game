import pygame, sys
from game import Game 
from mycolors import MyColors

pygame.init()
title_font= pygame.font.Font(None, 40)
score_surface= title_font.render("Score", True, MyColors.white)
next_surface= title_font.render("Next", True, MyColors.white)
game_over_surface= title_font.render("GAME OVER", True, MyColors.white)

score_rect= pygame.Rect(320, 55, 170, 60)
next_rect= pygame.Rect(320, 215, 170, 180)

screen= pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock= pygame.time.Clock()

game= Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

# Main game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    #Drawing
    score_value_surface = title_font.render(str(game.score), True, MyColors.white)

    screen.fill(MyColors.dark_blue)     
    screen.blit(score_surface, (365, 20, 50, 50)) 
    screen.blit(next_surface, (375, 180, 50, 50))
   
    if game.game_over:
        screen.blit(game_over_surface, (320, 450))
    pygame.draw.rect(screen, MyColors.light_blue, score_rect, 0, 10)     
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx= score_rect.centerx,
        centery= score_rect.centery))
    pygame.draw.rect(screen, MyColors.light_blue, next_rect, 0, 10)
    game.draw(screen)   
    #ame.move_down()

    pygame.display.update()
    clock.tick(60)                   

    