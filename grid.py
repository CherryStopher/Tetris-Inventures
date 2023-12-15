import pygame
from consts import COLORS, MIDNIGHT_BLUE, WHITE
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_ROWS, GRID_COLS, GRID_CELL_SIZE


class Grid:
    def __init__(self):
        self.rows = GRID_ROWS
        self.cols = GRID_COLS
        self.cell_size = GRID_CELL_SIZE
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size

    def reset_grid(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def is_valid_position(self, row, col):
        return (0 <= row and row < self.rows) and (0 <= col and col < self.cols)

    def is_valid_playable_position(self, row, col):
        return (2 <= row and row < self.rows) and (0 <= col and col < self.cols)

    def is_empty_cell(self, row, col):
        return self.grid[row][col] == 0

    def all_blocks_are_valid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != 0 and row < 2:
                    print(row, col, self.grid[row][col])
                    return False
        return True

    def clear_lines(self):
        lines_cleared = 0
        for row in range(self.rows):
            if 0 not in self.grid[row]:
                self.grid.pop(row)
                self.grid.insert(0, [0 for _ in range(self.cols)])
                lines_cleared += 1
        return lines_cleared

    def draw(self, screen):
        # Grid
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    col * self.cell_size + SCREEN_WIDTH / 2 - self.width / 2,
                    row * self.cell_size + SCREEN_HEIGHT / 2 - self.height / 2,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, COLORS[cell_value], cell_rect, 0)

    def draw_border(self, screen):
        # Top border
        rect_width = self.width
        rect_height = self.cell_size * 4 - 12
        rect_top = SCREEN_HEIGHT / 2 - self.height / 2
        center_rect_size = min(self.width, self.height) // 2
        center_rect = pygame.Rect(
            SCREEN_WIDTH / 2 - rect_width / 2, 0, rect_width, rect_height
        )
        pygame.draw.rect(screen, MIDNIGHT_BLUE, center_rect)
