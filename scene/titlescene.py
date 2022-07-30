import pygame
import json
from scene.scene import Scene
from scene.levelscene import LevelScene
from ui.button import Button


class TitleScene(Scene):
    def __init__(self):
        self.logo = pygame.image.load(r'ui/ui-graphics/logo.png').convert()
        self.start = Button("start", self.switch_to_level, 50, 150, 150, 20)
        self.font = pygame.font.SysFont("Calibri", 14)
        self.highscore = 0
        self.next = self

    def buttons(self):
        return [self.start]

    def highscore_text(self):
        return self.font.render(f"High score: {self.highscore}", 0, (255, 255, 255))

    def update(self, delta):
        self.highscore = json.load(open('config.json'))['high-score']

    def process_input(self, events):
        for button in self.buttons():
            button.process_input(events)

    def render(self, screen):
        hs = self.highscore_text()
        screen.blit(hs, hs.get_rect(center=(50, 125)))
        screen.blit(self.logo, self.logo.get_rect(topleft=(50, 20)))
        for button in self.buttons():
            button.render(screen)

    def switch_to_level(self):
        self.next = LevelScene()
