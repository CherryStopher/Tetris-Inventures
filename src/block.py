import pygame
from .settings import *
from .position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.color = COLORS[self.id]
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0

        self.initial_row_offset = 2
        self.initial_col_offset = 3

        self.row_offset = self.initial_row_offset
        self.col_offset = self.initial_col_offset

        self.ghost_row_offset = self.initial_row_offset
        self.ghost_col_offset = self.initial_col_offset

    def set_initial_offsets(self, plus_row_offset=0, plus_col_offset=0):
        self.row_offset = self.initial_row_offset + plus_row_offset
        self.col_offset = self.initial_col_offset + plus_col_offset
        self.ghost_row_offset = self.initial_row_offset + plus_row_offset
        self.ghost_col_offset = self.initial_col_offset + plus_col_offset

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            new_position = Position(
                position.row + self.row_offset, position.col + self.col_offset
            )
            moved_tiles.append(new_position)
        return moved_tiles

    def get_ghost_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            new_position = Position(
                position.row + self.ghost_row_offset,
                position.col + self.ghost_col_offset,
            )
            moved_tiles.append(new_position)
        return moved_tiles

    def get_offsets(self):
        return (self.row_offset, self.col_offset)

    def set_ghost_offsets(self, row, col):
        self.ghost_row_offset = row
        self.ghost_col_offset = col

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols
        self.move_ghost(0, cols)

    def move_ghost(self, rows, cols):
        self.ghost_row_offset += rows
        self.ghost_col_offset += cols

    def restart_block(self, plus_row_offset=0, plus_col_offset=0):
        self.rotation_state = 0
        self.set_initial_offsets(plus_row_offset, plus_col_offset)
        if self.id == 1:  # IBlock
            self.move(-1, 0)
            self.move_ghost(-1, 0)
        elif self.id == 4:  # OBlock
            self.move(0, 1)

    def rotate_clockwise(self):
        self.rotation_state = (self.rotation_state + 1) % 4

    def rotate_counter_clockwise(self):
        self.rotation_state = (self.rotation_state - 1) % 4

    def draw(self, screen, offset_x=0, offset_y=0):
        # Ghost block
        tiles = self.get_ghost_cell_positions()
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
            pygame.draw.rect(screen, self.color, tile_rect, 4)

        # Block
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
