from pygame.time import get_ticks


class Timer:
    def __init__(self, speed, repeat=False, func=None):
        self.repeat = repeat
        self.func = func
        self.speed = speed

        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = (
            get_ticks()
        )  # the time elapsed since the start of the game (pygame.init())

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):  # called every frame
        current_time = get_ticks()
        if self.active and current_time - self.start_time >= self.speed:
            # call the function
            if self.func and self.start_time != 0:
                self.func()

            # reset timer
            self.deactivate()

            # repeat the timer
            if self.repeat:
                self.activate()
