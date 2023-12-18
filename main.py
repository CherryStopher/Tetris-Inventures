import pygame, sys
from game import Game
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MIDNIGHT_BLUE, WHITE, LIGHT_BLUE


pygame.init()

# Font
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, WHITE)
score_rect = pygame.Rect(SCREEN_WIDTH - 200, 100, 170, 60)


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")


clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT
speed = game.get_speed()
pygame.time.set_timer(GAME_UPDATE, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game.end:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate_clockwise()
                if event.key == pygame.K_z or event.key == pygame.K_LCTRL:
                    game.rotate_counter_clockwise()
                if (
                    event.key == pygame.K_c
                    or event.key == pygame.K_LSHIFT
                    or event.key == pygame.K_RSHIFT
                ):
                    game.store_block()
                if event.key == pygame.K_SPACE:
                    game.hard_drop()
            if event.key == pygame.K_r and game.end:
                game.reset()
        if game.end:
            game.game_over()

    # Update falling blocks
    game.update_natural_movement()

    # Draw
    screen.fill(MIDNIGHT_BLUE)

    game.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
