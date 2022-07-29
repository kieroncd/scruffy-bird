import pygame


class Button:

    def __init__(self, text, func, x, y, sx, sy):
        self.x, self.y = x, y
        self.sx, self.sy = sx, sy
        self.func = func
        self.color = (0, 0, 255)
        self.rect = pygame.Rect((x, y), (sx, sy))
        self.text = text

    def update(self):
        pass

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def process_input(self, events):
        self.color = (0, 0, 255)
        if self.is_hovering():
            self.color = (0, 255, 0)
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.func()

    def is_hovering(self):
        x, y = pygame.mouse.get_pos()
        if self.x < x < self.x + self.sx and self.y < y < self.y + self.sy:
            return True
        return False