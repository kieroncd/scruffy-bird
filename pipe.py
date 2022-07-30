import pygame
import numpy as np


class Pipe:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), (50, 200))

    def update(self, delta, speed=0.1):
        self.x -= speed * delta
        self.rect = pygame.Rect((self.x, self.y), (50, 200))

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)


class PipePair:

    def __init__(self, x):
        self.x = x
        self.award_points = True
        offset = np.random.randint(-100, 100)
        self.upper = Pipe(self.x, -100 + offset)
        self.lower = Pipe(self.x, 200 + offset)

    def update(self, delta, speed=0.1):
        self.check_oob()
        self.upper.update(delta, speed)
        self.lower.update(delta, speed)
        self.x = self.upper.x

    def render(self, screen):
        self.upper.render(screen)
        self.lower.render(screen)

    def check_oob(self):
        # Checks if pipe is off-screen
        if self.x < -50:
            return True

    def reposition(self, x):
        offset = np.random.randint(-100, 100)
        self.upper.x = x
        self.upper.y = -100 + offset
        self.lower.x = x
        self.lower.y = 200 + offset
        self.x = x
        self.award_points = True
