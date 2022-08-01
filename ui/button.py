import pygame


class Button:

    def __init__(self, sprite, func, x, y, sx, sy, func_args=[]):
        self.x, self.y = x, y
        self.sx, self.sy = sx, sy  # button dimensions
        self.func = func
        self.func_args = func_args
        self.rect = pygame.Rect((x, y), (sx, sy))
        self.sprite = pygame.image.load(f'ui/ui-graphics/{sprite}.png').convert()
        self.hover_sprite = pygame.image.load(f'ui/ui-graphics/{sprite}_hover.png').convert()
        self.active_sprite = self.sprite

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.active_sprite, self.active_sprite.get_rect(topleft=(self.x, self.y)))

    def process_input(self, events):
        self.active_sprite = self.sprite
        if self.is_hovering():
            self.active_sprite = self.hover_sprite
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.func(*self.func_args)

    def is_hovering(self):
        x, y = pygame.mouse.get_pos()
        if self.x < x < self.x + self.sx and self.y < y < self.y + self.sy:
            return True
        return False
