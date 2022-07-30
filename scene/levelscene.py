import pygame
from scene.scene import Scene
from bird import Bird
from pipe import PipePair


def check_ready(events):
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return True
    return False


class LevelScene(Scene):

    def __init__(self):
        self.next = self
        self.player = Bird()
        self.pipe_one = PipePair(300)
        self.pipe_two = PipePair(500)
        self.score = 0
        self.ready = False

    def entities(self):
        return [self.player, self.pipe_one, self.pipe_two]

    def pipes(self):
        return [self.pipe_one, self.pipe_two]

    def update(self, delta):
        if not self.ready:
            return
        for e in self.entities():
            e.update(delta)
        self.check_collisions()
        self.reposition_obstacles()
        pygame.display.set_caption(f'{self.score}')

    def process_input(self, events):
        if not self.ready:
            self.ready = check_ready(events)
            return
        self.player.process_input(events)

    def render(self, screen):
        if not self.ready:
            press = pygame.image.load(r'ui/ui-graphics/pressspace.png').convert()
            screen.blit(press, press.get_rect(topleft=(25, 200)))
            return
        for e in self.entities():
            e.render(screen)

    def check_collisions(self):
        # if player falls off the bottom, reset
        if self.player.rect.y > 300:
            self.switch_scene(LevelScene())
        # checks collision of player with pipes
        for pipe in self.pipes():
            if self.player.rect.colliderect(pipe.upper.rect) or self.player.rect.colliderect(pipe.lower.rect):
                self.switch_scene(LevelScene())
                return
            if pipe.x < self.player.x and pipe.award_points:
                self.score += 1
                pipe.award_points = False

    def reposition_obstacles(self):
        if self.pipe_one.check_oob():
            self.pipe_one.reposition(self.pipe_two.x + 200)
        if self.pipe_two.check_oob():
            self.pipe_two.reposition(self.pipe_one.x + 200)

