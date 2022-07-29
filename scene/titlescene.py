import pygame
from scene.scene import Scene
from scene.levelscene import LevelScene
from ui.button import Button


class TitleScene(Scene):
    def __init__(self):
        self.logo = pygame.image.load(r'ui/ui-graphics/logo.png').convert()
        self.button = Button("start", self.l, 50, 150, 150, 20)
        self.next = self

    def update(self, delta):
        pass

    def process_input(self, events):
        self.button.process_input(events)

    def render(self, screen):
        screen.blit(self.logo, self.logo.get_rect(topleft=(50, 20)))
        self.button.render(screen)

    def l(self):
        self.next = LevelScene()
