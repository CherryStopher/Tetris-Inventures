import pygame
from consts import COLORS
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_ROWS, GRID_COLS, GRID_CELL_SIZE


class Grid:
    def __init__(self):
        self.rows = GRID_ROWS
        self.cols = GRID_COLS
        self.cell_size = GRID_CELL_SIZE
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size

    def is_valid_position(self, row, col):
        return (0 <= row and row < self.rows) and (0 <= col and col < self.cols)

    def is_empty_cell(self, row, col):
        return self.grid[row][col] == 0

    def clear_lines(self):
        lines_cleared = 0
        for row in range(self.rows):
            if 0 not in self.grid[row]:
                self.grid.pop(row)
                self.grid.insert(0, [0 for _ in range(self.cols)])
                lines_cleared += 1
        return lines_cleared

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col * self.cell_size + SCREEN_WIDTH / 2 - self.width / 2,
                    row * self.cell_size + SCREEN_HEIGHT / 2 - self.height / 2,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, COLORS[cell_value], cell_rect)
