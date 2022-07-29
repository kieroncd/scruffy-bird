import numpy as np
import pygame


class Bird:

    def __init__(self, x=100, y=150, a=0.01, debug=False):
        self.x = x
        self.y = y
        self.v = 0
        self.a = a  # gravity strength
        self.sprite = pygame.image.load(r'graphics/scruff.png').convert()
        self.rect = self.sprite.get_rect()
        self.rect.center = (100, 150)
        self.debug = debug
        if self.debug:
            self.upper_dot = pygame.Rect((self.x, self.y), (25, 1))
            self.lower_dot = pygame.Rect((self.x, self.y + 25), (25, 1))

    def update(self, delta):
        self.v += self.a * delta
        self.y += self.v
        self.rect = self.sprite.get_rect()
        self.rect.center = (100, self.y)
        if self.debug:
            self.upper_dot = pygame.Rect((self.x, self.y), (25, 1))
            self.lower_dot = pygame.Rect((self.x, self.y + 25), (25, 1))
        self.a = 0.01

    def render(self, screen):
        screen.blit(self.sprite, self.rect)
        if self.debug:
            pygame.draw.rect(screen, (255, 0, 0), self.upper_dot)
            pygame.draw.rect(screen, (255, 0, 0), self.lower_dot)

    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.v = -4
