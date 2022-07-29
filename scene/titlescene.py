import pygame
from scene.scene import Scene
from scene.levelscene import LevelScene
from ui.button import Button


class TitleScene(Scene):
    def __init__(self):
        self.button = Button("start", self.l, 100, 100, 100, 20)
        self.next = self

    def update(self, delta):
        pass

    def process_input(self, events):
        self.button.process_input(events)

    def render(self, screen):
        self.button.render(screen)

    def l(self):
        self.next = LevelScene()
