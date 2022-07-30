import pygame


class UIElement:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self):
        pass

    def render(self, screen):
        pass


class ScoreCounter(UIElement):

    def __init__(self, x=125, y=40):
        self.font = pygame.font.SysFont("Impact", 24)
        self.score = 0
        self.x, self.y = x, y

    def add_score(self, amount=1):
        self.score += amount

    def score_text(self):
        return self.font.render(f"{self.score}", 0, (255, 255, 255))

    def render(self, screen):
        st = self.score_text()
        screen.blit(st, st.get_rect(center=(self.x, self.y)))


class LevelUI:

    def __init__(self):
        self.score_counter = ScoreCounter()

    def update(self):
        self.score_counter.update()

    def render(self, screen):
        self.score_counter.render(screen)
