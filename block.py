import pygame
from consts import (
    COLORS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_ROWS,
    GRID_COLS,
    GRID_CELL_SIZE,
)
from position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.color = COLORS[self.id]
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0

        self.row_offset = 0
        self.col_offset = 3

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            new_position = Position(
                position.row + self.row_offset, position.col + self.col_offset
            )
            moved_tiles.append(new_position)
        return moved_tiles

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def restart_block(self):
        self.rotation_state = 0
        self.row_offset = 0
        self.col_offset = 3
        if self.id == 1:  # IBlock
            self.move(-1, 0)
        elif self.id == 4:  # OBlock
            self.move(0, 1)

    def rotate_clockwise(self):
        self.rotation_state = (self.rotation_state + 1) % 4

    def rotate_counter_clockwise(self):
        self.rotation_state = (self.rotation_state - 1) % 4

    def draw(self, screen, offset_x=0, offset_y=0):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x
                + tile.col * self.cell_size
                + SCREEN_WIDTH / 2
                - GRID_COLS * GRID_CELL_SIZE / 2,
                offset_y
                + tile.row * self.cell_size
                + SCREEN_HEIGHT / 2
                - GRID_ROWS * GRID_CELL_SIZE / 2,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.color, tile_rect)
