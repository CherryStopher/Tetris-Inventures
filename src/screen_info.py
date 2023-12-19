import pygame
from .settings import *


class ScreenInfo:
    def __init__(self):
        self.level = 1
        self.lines = 0
        self.score = 0
        self.combo = 0

        self.x_offset = 60
        self.y_offset = 250

        self.next_blocks = []

        # Info rect
        self.info_rect = pygame.Rect(
            INFO_RECT_X,
            INFO_RECT_Y,
            INFO_RECT_WIDTH,
            INFO_RECT_HEIGHT,
        )
        self.next_blocks_rect = pygame.Rect(
            NEXT_RECT_X,
            NEXT_RECT_Y,
            NEXT_RECT_WIDTH,
            NEXT_RECT_HEIGHT,
        )
        self.stored_block_rect = pygame.Rect(
            STORED_RECT_X,
            STORED_RECT_Y,
            STORED_RECT_WIDTH,
            STORED_RECT_HEIGHT,
        )
        self.combo_rect = pygame.Rect(
            COMBO_RECT_X,
            COMBO_RECT_Y,
            COMBO_RECT_WIDTH,
            COMBO_RECT_HEIGHT,
        )
        self.lines_rect = pygame.Rect(
            LINES_RECT_X,
            LINES_RECT_Y,
            LINES_RECT_WIDTH,
            LINES_RECT_HEIGHT,
        )

        # Text
        self.font = pygame.font.Font(None, 40)

        self.stored_next = self.font.render("STORED", True, WHITE)

        self.combo_text = self.font.render("COMBO", True, WHITE)
        self.combo_number_text = self.font.render(f"{self.lines}", True, WHITE)

        self.lines_text = self.font.render("LINES", True, WHITE)
        self.lines_number_text = self.font.render(f"{self.lines}/10", True, WHITE)

        self.next_text = self.font.render("NEXT", True, WHITE)

        self.level_text = self.font.render("LEVEL", True, WHITE)
        self.level_number_text = self.font.render(f"{self.level}", True, WHITE)

        self.score_text = self.font.render("SCORE", True, WHITE)
        self.score_number_text = self.font.render(f"{self.score}", True, WHITE)

        self.high_score_text = self.font.render("HIGH SCORE", True, WHITE)
        self.high_score_number_text = self.font.render(f"{self.score}", True, WHITE)

        self.game_over_text = self.font.render("GAME OVER", True, WHITE)
        self.restart_text = self.font.render("Press R to restart", True, WHITE)

    def set_score(self, score):
        self.score = score
        self.score_number_text = self.font.render(f"{self.score}", True, WHITE)

    def set_high_score(self, score):
        self.high_score = score
        self.high_score_number_text = self.font.render(
            f"{self.high_score}", True, WHITE
        )

    def set_level(self, level):
        self.level = level
        self.level_number_text = self.font.render(f"{self.level}", True, WHITE)

    def set_lines(self, lines):
        self.lines = lines
        self.lines_number_text = self.font.render(f"{self.lines}/10", True, WHITE)

    def set_next_blocks(self, next_blocks):
        self.next_blocks = next_blocks

    def set_combo(self, combo):
        self.combo = combo
        self.combo_number_text = self.font.render(f"{self.combo}", True, WHITE)

    def draw_text(self, screen, text, x, y):
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def draw(self, screen, end, three_next_blocks, stored_block):
        # Info rect
        pygame.draw.rect(screen, MIDNIGHT_BLUE, self.info_rect, 0)
        pygame.draw.rect(screen, MIDNIGHT_BLUE, self.next_blocks_rect, 0)
        pygame.draw.rect(screen, MIDNIGHT_BLUE, self.stored_block_rect, 0)
        pygame.draw.rect(screen, MIDNIGHT_BLUE, self.combo_rect, 0)
        pygame.draw.rect(screen, MIDNIGHT_BLUE, self.lines_rect, 0)

        # End game
        if end:
            screen.blit(
                self.game_over_text,
                (
                    SCREEN_WIDTH / 2 - self.game_over_text.get_width() / 2,
                    20,
                ),
            )
            screen.blit(
                self.restart_text,
                (
                    SCREEN_WIDTH / 2 - self.restart_text.get_width() / 2,
                    60,
                ),
            )

        # Next blocks
        for i, block in enumerate(three_next_blocks):
            if block.id == 1:  # IBlock
                block.draw(
                    screen,
                    GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 75,
                    60 + 90 * i,
                )
            elif block.id == 4:  # OBlock
                block.draw(
                    screen,
                    GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 75,
                    45 + 90 * i,
                )
            else:
                block.draw(
                    screen,
                    GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 90,
                    45 + 90 * i,
                )

        # Stored text
        screen.blit(
            self.stored_next,
            (
                STORED_RECT_X + 65,
                STORED_RECT_Y + 30,
            ),
        )

        # Stored block
        if stored_block:
            if stored_block.id == 1:  # IBlock
                stored_block.draw(
                    screen,
                    -(GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 90),
                    STORED_RECT_Y + 15,
                )
            elif stored_block.id == 4:  # OBlock
                stored_block.draw(
                    screen,
                    -(GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 90),
                    STORED_RECT_Y,
                )
            else:
                stored_block.draw(
                    screen,
                    -(GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset + 75),
                    STORED_RECT_Y,
                )

        # Combo text
        if self.combo > 0:
            screen.blit(
                self.combo_text,
                (
                    COMBO_RECT_X + 75,
                    COMBO_RECT_Y + 30,
                ),
            )
            screen.blit(
                self.combo_number_text,
                (
                    COMBO_RECT_X + 75,
                    COMBO_RECT_Y + 75,
                ),
            )

        # Lines cleared text
        screen.blit(
            self.lines_text,
            (
                LINES_RECT_X + 75,
                LINES_RECT_Y + 30,
            ),
        )
        screen.blit(
            self.lines_number_text,
            (
                LINES_RECT_X + 75,
                LINES_RECT_Y + 75,
            ),
        )

        right_info = [
            self.level_text,
            self.level_number_text,
            self.score_text,
            self.score_number_text,
            self.high_score_text,
            self.high_score_number_text,
        ]

        for i, text in enumerate(right_info):
            screen.blit(
                text,
                (
                    SCREEN_WIDTH / 2 + GRID_COLS * GRID_CELL_SIZE / 2 + self.x_offset,
                    20 + INFO_RECT_Y + 40 * i,
                ),
            )

        # Next blocks text
        screen.blit(
            self.next_text,
            (
                NEXT_RECT_X + 75,
                10 + NEXT_RECT_Y,
            ),
        )
