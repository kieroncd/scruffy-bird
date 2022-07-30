import pygame
from scene.scene import Scene
from scene.levelscene import LevelScene
from ui.button import Button


class TitleScene(Scene):
    def __init__(self):
        self.logo = pygame.image.load(r'ui/ui-graphics/logo.png').convert()
        self.start = Button("start", self.switch_to_level, 50, 150, 150, 20)
        self.next = self

    def buttons(self):
        return [self.start]

    def update(self, delta):
        pass

    def process_input(self, events):
        for button in self.buttons():
            button.process_input(events)

    def render(self, screen):
        screen.blit(self.logo, self.logo.get_rect(topleft=(50, 20)))
        for button in self.buttons():
            button.render(screen)

    def switch_to_level(self):
        self.next = LevelScene()
