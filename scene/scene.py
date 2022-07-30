import pygame


class Scene:

    def __init__(self):
        self.next = self

    def process_input(self, events):
        raise NotImplementedError(f"process_input not implemented in {self.__class__.__name__}")

    def update(self, delta):
        raise NotImplementedError(f"update not implemented in {self.__class__.__name__}")

    def render(self, screen):
        raise NotImplementedError(f"render not implemented in {self.__class__.__name__}")

    def switch_scene(self, next_scene):
        self.next = next_scene

    def kill(self):
        self.next = None
