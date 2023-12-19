import pygame, sys
from src.game import Game
from src.settings import *


class Main:
    def __init__(self):
        pygame.init()

        # Create the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()

        self.game = Game()
        GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(GAME_UPDATE, 200)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if not self.game.end:
                        if event.key == pygame.K_LEFT:
                            self.game.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.game.move_right()
                        if event.key == pygame.K_DOWN:
                            self.game.move_down()
                            self.game.update_score(0, 1)
                        if event.key == pygame.K_UP:
                            self.game.rotate_clockwise()
                        if event.key == pygame.K_z or event.key == pygame.K_LCTRL:
                            self.game.rotate_counter_clockwise()
                        if (
                            event.key == pygame.K_c
                            or event.key == pygame.K_LSHIFT
                            or event.key == pygame.K_RSHIFT
                        ):
                            self.game.store_block()
                        if event.key == pygame.K_SPACE:
                            self.game.hard_drop()
                    if event.key == pygame.K_r and self.game.end:
                        self.game.reset()

            # Update falling blocks
            if not self.game.end:
                self.game.update_natural_movement()

            # Draw
            self.screen.fill(DENIM_BLUE)

            self.game.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    main = Main()
    main.run()
