from grid import Grid
from screen_info import ScreenInfo
from tetrominoes import *
import random
import pygame


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = []
        self.fill_bag()

        self.current_block = self.get_random_block()
        self.next_1st_block = self.get_random_block()
        self.next_2nd_block = self.get_random_block()
        self.next_3rd_block = self.get_random_block()

        self.screen_info = ScreenInfo()
        self.screen_info.set_next_blocks(self.get_three_next_blocks())

        self.end = False
        self.score = 0
        self.lines = 0
        self.level = 1

        pygame.mixer.music.load("Tetris.mp3")
        pygame.mixer.music.play(-1)

    def fill_bag(self):
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            ZBlock(),
            TBlock(),
        ]

    def get_three_next_blocks(self):
        return [self.next_1st_block, self.next_2nd_block, self.next_3rd_block]

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.fill_bag()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def is_block_inside_grid(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_valid_position(tile.row, tile.col):
                return False
        return True

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.current_block.id

        self.current_block = self.next_1st_block
        self.next_1st_block = self.next_2nd_block
        self.next_2nd_block = self.next_3rd_block
        self.next_3rd_block = self.get_random_block()
        self.screen_info.set_next_blocks(self.get_three_next_blocks())

        lines_cleared = self.grid.clear_lines()
        self.update_lines(lines_cleared)
        self.update_score(lines_cleared, 0)

        if not self.is_block_inside_grid() or not self.block_fits():
            self.end = True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty_cell(tile.row, tile.col):
                return False
        return True

    # Movement
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def rotate_clockwise(self):
        self.current_block.rotate_clockwise()
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.rotate_counter_clockwise()

    def rotate_counter_clockwise(self):
        self.current_block.rotate_counter_clockwise()
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.rotate_clockwise()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        self.screen_info.draw(screen, self.end, self.get_three_next_blocks())

    def reset(self):
        self.grid = Grid()
        self.fill_bag()
        self.current_block = self.get_random_block()
        self.next_1st_block = self.get_random_block()
        self.next_2nd_block = self.get_random_block()
        self.next_3rd_block = self.get_random_block()
        self.screen_info.set_next_blocks(self.get_three_next_blocks())

        self.end = False
        self.score = 0
        self.lines = 0
        self.level = 1

        self.screen_info.set_score(self.score)
        self.screen_info.set_lines(self.lines)
        self.screen_info.set_level(self.level)

    def update_score(self, lines_cleared, moved_down_cells):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
        self.score += moved_down_cells
        self.screen_info.set_score(self.score)

    def update_lines(self, lines_cleared):
        self.lines += lines_cleared
        self.screen_info.set_lines(self.lines)