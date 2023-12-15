import pygame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_COLS, GRID_CELL_SIZE, WHITE


class ScreenInfo:
    def __init__(self):
        self.level = 1
        self.lines = 0
        self.score = 0

        self.x_offset = 100
        self.y_offset = 250

        self.next_blocks = []
        # self.stored_block = None

        self.font = pygame.font.Font(None, 40)

        self.stored_next = self.font.render("STORED", True, WHITE)

        self.lines_text = self.font.render("LINES", True, WHITE)
        self.lines_number_text = self.font.render(f"{self.lines}/10", True, WHITE)

        self.next_text = self.font.render("NEXT", True, WHITE)

        self.level_text = self.font.render("LEVEL", True, WHITE)
        self.level_number_text = self.font.render(f"{self.level}", True, WHITE)

        self.score_text = self.font.render("SCORE", True, WHITE)
        self.score_number_text = self.font.render(f"{self.score}", True, WHITE)

        self.game_over_text = self.font.render("GAME OVER", True, WHITE)

    def set_score(self, score):
        self.score = score
        self.score_number_text = self.font.render(f"{self.score}", True, WHITE)

    def set_level(self, level):
        self.level = level
        self.level_number_text = self.font.render(f"{self.level}", True, WHITE)

    def set_lines(self, lines):
        self.lines = lines
        self.lines_number_text = self.font.render(f"{self.lines}/10", True, WHITE)

    def set_next_blocks(self, next_blocks):
        self.next_blocks = next_blocks

    # def set_stored_block(self, stored_block):
    #     self.stored_block = stored_block

    def draw(self, screen, end, three_next_blocks, stored_block, win=False):
        # End game
        if end:
            screen.blit(
                self.game_over_text,
                (
                    SCREEN_WIDTH / 2 - self.game_over_text.get_width() / 2,
                    SCREEN_HEIGHT - 40,
                ),
            )

        # Stored block
        if stored_block:
            stored_block.draw(
                screen,
                -(GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 90),
                90,
            )

        # Next blocks
        for i, block in enumerate(three_next_blocks):
            if block.id == 1:  # IBlock
                block.draw(
                    screen,
                    GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 45,
                    75 + 90 * i,
                )
            elif block.id == 4:  # OBlock
                block.draw(
                    screen,
                    GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 45,
                    60 + 90 * i,
                )
            else:
                block.draw(
                    screen,
                    GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 60,
                    60 + 90 * i,
                )

        screen.blit(
            self.stored_next,
            (
                self.x_offset,
                self.y_offset - 150,
            ),
        )
        screen.blit(
            self.lines_text,
            (
                self.x_offset,
                SCREEN_HEIGHT - self.y_offset,
            ),
        )
        screen.blit(
            self.lines_number_text,
            (
                self.x_offset,
                SCREEN_HEIGHT - self.y_offset + 40,
            ),
        )
        screen.blit(
            self.next_text,
            (
                SCREEN_WIDTH / 2 + GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset,
                self.y_offset - 150,
            ),
        )
        screen.blit(
            self.level_text,
            (
                SCREEN_WIDTH / 2 + GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset,
                SCREEN_HEIGHT - self.y_offset,
            ),
        )
        screen.blit(
            self.level_number_text,
            (
                SCREEN_WIDTH / 2 + GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset,
                SCREEN_HEIGHT - self.y_offset + 40,
            ),
        )
        screen.blit(
            self.score_text,
            (
                SCREEN_WIDTH / 2 + GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset,
                SCREEN_HEIGHT - self.y_offset + 100,
            ),
        )
        screen.blit(
            self.score_number_text,
            (
                SCREEN_WIDTH / 2 + GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset,
                SCREEN_HEIGHT - self.y_offset + 140,
            ),
        )
