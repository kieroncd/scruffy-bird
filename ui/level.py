import pygame
from ui.uielement import UIElement
from ui.outlinetext import OutlinedText


class ScoreCounter(UIElement):

    def __init__(self, x=125, y=40):
        self.score = 0
        self.x, self.y = x, y
        self.counter = OutlinedText(f"{self.score}", pygame.font.SysFont("Impact", 24), x=self.x, y=self.y)

    def add_score(self, amount=1):
        self.score += amount
        self.counter.text = f'{self.score}'

    def score_text(self):
        return self.font.render(f"{self.score}", 0, (0, 0, 0))

    def update(self):
        self.counter.update()

    def render(self, screen):
        self.counter.render(screen)


class LevelUI:

    def __init__(self):
        self.score_counter = ScoreCounter()

    def update(self):
        self.score_counter.update()

    def render(self, screen):
        self.score_counter.render(screen)
