from grid import Grid
from screen_info import ScreenInfo
from tetrominoes import *
from timer import Timer
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

        self.update_ghost_block()

        self.stored_block = None
        self.can_store = True

        self.screen_info = ScreenInfo()
        self.screen_info.set_next_blocks(self.get_three_next_blocks())

        self.end = False
        self.win = False
        self.score = 0
        self.lines = 0
        self.level = 1
        self.combo = -1

        # 1000ms = 1s
        self.speed = 1000 * ((0.8 - ((self.level - 1) * 0.007)) ** (self.level - 1))
        self.timer = Timer(self.speed, repeat=True, func=self.move_down)
        self.timer.activate()

        pygame.mixer.music.load("Tetris.mp3")
        # pygame.mixer.music.play(-1)

    def reset(self):
        self.grid = Grid()
        self.fill_bag()
        self.current_block = self.get_random_block()
        self.next_1st_block = self.get_random_block()
        self.next_2nd_block = self.get_random_block()
        self.next_3rd_block = self.get_random_block()
        self.screen_info.set_next_blocks(self.get_three_next_blocks())

        self.update_ghost_block()

        self.stored_block = None

        self.end = False
        self.win = False
        self.score = 0
        self.lines = 0
        self.level = 1
        self.combo = -1

        self.screen_info.set_score(self.score)
        self.screen_info.set_lines(self.lines)
        self.screen_info.set_level(self.level)

        self.speed = 1000 * ((0.8 - ((self.level - 1) * 0.007)) ** (self.level - 1))
        self.timer = Timer(self.speed, repeat=True, func=self.move_down)
        self.timer.activate()

        # pygame.mixer.music.play(-1)

    def fill_bag(self):
        # self.blocks = [
        #     IBlock(),
        #     JBlock(),
        #     LBlock(),
        #     OBlock(),
        #     SBlock(),
        #     ZBlock(),
        #     TBlock(),
        # ]
        self.blocks = [
            IBlock(),
            IBlock(),
            IBlock(),
            IBlock(),
            IBlock(),
        ]

    def get_three_next_blocks(self):
        return [self.next_1st_block, self.next_2nd_block, self.next_3rd_block]

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.fill_bag()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def update_next_blocks(self):
        self.next_1st_block = self.next_2nd_block
        self.next_2nd_block = self.next_3rd_block
        self.next_3rd_block = self.get_random_block()
        self.screen_info.set_next_blocks(self.get_three_next_blocks())

    def store_block(self):
        if self.can_store:
            self.can_store = False
            temp_block = self.current_block
            temp_block.restart_block()
            if self.stored_block == None:
                self.stored_block = temp_block
                self.current_block = self.next_1st_block

                if not self.block_fits():  # If it is at the spawn
                    self.fix_ghost_block()
                    if not self.is_block_inside_grid() or not self.block_fits():
                        self.end = True
                self.update_ghost_block()
                self.update_next_blocks()

            else:
                self.current_block = self.stored_block
                self.current_block.restart_block()

                if not self.block_fits():  # If it is at the spawn
                    self.fix_ghost_block()
                    if not self.is_block_inside_grid() or not self.block_fits():
                        self.end = True
                self.update_ghost_block()
                self.stored_block = temp_block

    def fix_ghost_block(self):
        while self.is_block_inside_grid() and not self.block_fits():
            self.current_block.move(-1, 0)
            self.update_ghost_block()

    def is_block_inside_grid(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_valid_position(tile.row, tile.col):
                return False
        return True

    def is_block_inside_playable_grid(self):
        tiles_inside = []
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_valid_playable_position(tile.row, tile.col):
                tiles_inside.append(False)
            else:
                tiles_inside.append(True)
        return all(tiles_inside)  # if all tiles are inside the playable grid

    def is_ghost_block_inside_grid(self):
        tiles = self.current_block.get_ghost_cell_positions()
        for tile in tiles:
            if not self.grid.is_valid_position(tile.row, tile.col):
                return False
        return True

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.current_block.id
        self.current_block = self.next_1st_block
        self.update_next_blocks()

        lines_cleared = self.grid.clear_lines()
        if lines_cleared == 0:
            self.combo = -1
        self.update_score(lines_cleared, 0)
        self.update_lines(lines_cleared)
        self.update_ghost_block()
        self.can_store = True

        # spawn block
        if not self.block_fits():  # If it is at the spawn
            while self.is_block_inside_grid() and not self.block_fits():
                self.current_block.move(-1, 0)
                self.update_ghost_block()
            if not self.is_block_inside_grid() or not self.block_fits():
                self.end = True
        if not self.grid.all_blocks_are_valid():
            self.end = True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty_cell(tile.row, tile.col):
                return False
        return True

    def ghost_block_fits(self):
        tiles = self.current_block.get_ghost_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty_cell(tile.row, tile.col):
                return False
        return True

    def update_ghost_block(self):
        block_offsets = self.current_block.get_offsets()
        self.current_block.set_ghost_offsets(block_offsets[0], block_offsets[1])
        while self.is_ghost_block_inside_grid() and self.ghost_block_fits():
            self.current_block.move_ghost(1, 0)
        self.current_block.move_ghost(-1, 0)

    # Movement
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.move(0, 1)
        self.update_ghost_block()

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.move(0, -1)
        self.update_ghost_block()

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()

    def hard_drop(self):
        rows = 0
        while self.is_block_inside_grid() and self.block_fits():
            self.current_block.move(1, 0)
            rows += 1
        self.current_block.move(-1, 0)
        rows -= 1
        self.lock_block()
        self.update_score(0, 2 * rows)

    # Rotation
    def rotate_clockwise(self):
        self.current_block.rotate_clockwise()
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.rotate_counter_clockwise()
        self.update_ghost_block()

    def rotate_counter_clockwise(self):
        self.current_block.rotate_counter_clockwise()
        if not self.is_block_inside_grid() or not self.block_fits():
            self.current_block.rotate_clockwise()
        self.update_ghost_block()

    # Update screen info
    def update_score(self, lines_cleared=None, moved_down_cells=0):
        lines_score = {1: 100, 2: 300, 3: 500, 4: 800}
        perfect_clear_line_score = {1: 800, 2: 1200, 3: 1600, 4: 2000}
        grid_is_empty = self.grid.grid_is_empty()

        # soft drop
        self.score += moved_down_cells

        # complete rows
        if lines_cleared:
            if grid_is_empty:
                self.score += perfect_clear_line_score[lines_cleared] * self.level
            else:
                self.combo += 1
                if self.combo > -1:
                    self.score += 50 * self.combo * self.level
                self.score += lines_score[lines_cleared] * self.level

        self.screen_info.set_score(self.score)

    def update_lines(self, lines_cleared):
        self.lines += lines_cleared
        if self.lines >= 10:
            self.level_up()
            self.screen_info.set_level(self.level)
        self.screen_info.set_lines(self.lines)

    def level_up(self):
        self.lines = 0
        self.level += 1
        self.speed = 1000 * ((0.8 - ((self.level - 1) * 0.007)) ** (self.level - 1))
        self.timer.set_speed(self.speed)
        self.screen_info.set_level(self.level)
        if self.level >= 10:
            self.win = True

    def get_level(self):
        return self.level

    def get_speed(self):
        return self.speed

    def update_natural_movement(self):
        if not self.end:
            self.timer.update()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        self.grid.draw_border(screen)
        self.screen_info.draw(
            screen, self.end, self.get_three_next_blocks(), self.stored_block, self.win
        )
