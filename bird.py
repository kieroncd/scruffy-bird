import pygame


class Bird:

    def __init__(self, x=100, y=150, a=0.01, debug=False):
        self.x = x
        self.y = y
        self.v = 0
        self.a = a  # gravity strength
        self.sprite = pygame.image.load(f'graphics/joe.png').convert()
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.debug = debug
        if self.debug:
            self.upper_dot = pygame.Rect((self.x, self.y), (25, 1))
            self.lower_dot = pygame.Rect((self.x, self.y + 25), (25, 1))

    def update(self, delta):
        self.v += self.a * delta
        self.y += self.v
        self.rect = self.sprite.get_rect(topleft=(100, self.y))
        if self.debug:
            self.upper_dot = pygame.Rect((self.x, self.y), (25, 1))
            self.lower_dot = pygame.Rect((self.x, self.y + 25), (25, 1))

    def render(self, screen):
        screen.blit(self.sprite, self.rect)
        if self.debug:
            pygame.draw.rect(screen, (255, 0, 0), self.upper_dot)
            pygame.draw.rect(screen, (255, 0, 0), self.lower_dot)

    def process_input(self, events):
        # TODO: implement fixed timestep impulse
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.v = -4
