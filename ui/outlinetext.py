import pygame
from ui.uielement import UIElement


class OutlinedText(UIElement):

    def __init__(self, text, font, x=0, y=0, colour=(255, 255, 255), outlinecolour=(0, 0, 0)):
        self.x, self.y = x, y
        self.font = font
        self.colour = colour
        self.outlinecolour = outlinecolour
        self.text = text
        self.text_render = self.font.render(text, 0, self.colour)
        self.text_rect = self.text_render.get_rect(center=(self.x, self.y))
        self.outlinetext = self.font.render(text, 0, outlinecolour)
        self.outlinerect = self.generate_outline_rect()

    def generate_outline_rect(self):
        return [self.outlinetext.get_rect(center=(self.x-1, self.y-1)),
                self.outlinetext.get_rect(center=(self.x-1, self.y+1)),
                self.outlinetext.get_rect(center=(self.x+1, self.y-1)),
                self.outlinetext.get_rect(center=(self.x+1, self.y+1))]

    def update(self):
        self.text_render = self.font.render(self.text, 0, self.colour)
        self.text_rect = self.text_render.get_rect(center=(self.x, self.y))
        self.outlinetext = self.font.render(self.text, 0, self.outlinecolour)
        self.outlinerect = self.generate_outline_rect()

    def render(self, screen):
        for i in self.outlinerect:
            screen.blit(self.outlinetext, i)
        screen.blit(self.text_render, self.text_rect)
