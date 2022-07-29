import pygame


class Scene:

    def __init__(self):
        self.next = self

    def process_input(self, events):
        pass

    def update(self, delta):
        pass

    def render(self, screen):
        pass

    def switch_scene(self, next_scene):
        self.next = next_scene

    def kill(self):
        self.next = None
