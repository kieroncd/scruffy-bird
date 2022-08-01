import pygame
import json
import gc
from bird import Bird
from pipe import PipePair
from ui.background import ScrollingBackground, Background
from ui.button import Button
from ui.level import LevelUI


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
        gc.collect()

    def kill(self):
        self.next = None


class TitleScene(Scene):

    def __init__(self):
        self.logo = pygame.image.load(r'ui/ui-graphics/logo.png').convert()
        self.background = ScrollingBackground(scroll_speed=0.005)
        self.start = Button("start", self.switch_scene, 50, 150, 150, 20, func_args=[GetReadyScene()])
        self.next = self

    def buttons(self):
        return [self.start]

    def update(self, delta):
        self.background.update(delta)

    def process_input(self, events):
        for button in self.buttons():
            button.process_input(events)

    def render(self, screen):
        self.background.render(screen)
        screen.blit(self.logo, self.logo.get_rect(topleft=(50, 20)))
        for button in self.buttons():
            button.render(screen)


class GetReadyScene(Scene):

    def __init__(self):
        self.next = self
        self.background = Background(x=-745)
        self.press = pygame.image.load(r'ui/ui-graphics/pressspace.png').convert()

    def update(self, delta):
        pass

    def render(self, screen):
        self.background.render(screen)
        screen.blit(self.press, self.press.get_rect(center=(125, 150)))

    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.switch_scene(LevelScene())


class LevelScene(Scene):

    def __init__(self):
        self.next = self
        self.player = Bird()
        self.pipe_one = PipePair(300)
        self.pipe_two = PipePair(500)
        self.background = ScrollingBackground(x=-745)
        self.ui = LevelUI()

        self.score = 0

    def entities(self):
        return [self.pipe_one, self.pipe_two, self.player]

    def pipes(self):
        return [self.pipe_one, self.pipe_two]

    def update(self, delta):
        for e in self.entities():
            e.update(delta)
        self.background.update(delta)
        self.check_collisions()
        self.reposition_obstacles()
        self.ui.update()
        self.score = self.ui.score_counter.score

    def process_input(self, events):
        self.player.process_input(events)

    def render(self, screen):
        self.background.render(screen)
        for e in self.entities():
            e.render(screen)
        self.ui.render(screen)

    def check_collisions(self):
        # if player is out of bounds, game over
        if self.player.rect.y > 300 or self.player.rect.y < -50:
            self.switch_scene(GameOverScene(self))

        for pipe in self.pipes():
            # checks collision of player with pipes
            if self.player.rect.colliderect(pipe.upper.rect) or self.player.rect.colliderect(pipe.lower.rect):
                self.switch_scene(GameOverScene(self))
                return
            # score incrementation
            if pipe.x < self.player.x and pipe.award_points:
                self.ui.score_counter.add_score()
                pipe.award_points = False

    def reposition_obstacles(self):
        if self.pipe_one.check_oob():
            self.pipe_one.reposition(self.pipe_two.x + 200)
        if self.pipe_two.check_oob():
            self.pipe_two.reposition(self.pipe_one.x + 200)


class GameOverScene(Scene):
    # TODO: clean this code up
    def __init__(self, level_scene):
        self.next = self
        self.level_scene = level_scene
        self.player = level_scene.player
        self.background = level_scene.background
        self.background.scrolling_speed = 0
        with open("config.json", "r") as file:
            self.data = json.load(file)
        self.hs = self.data['high-score']
        self.font = pygame.font.SysFont("Impact", 24)
        self.gameoverstr = [f"Game Over!", f"Score: {level_scene.score}", f"Previous High Score: {self.hs}"]
        self.gameovertext = self.gameovertextgen(self.gameoverstr)
        self.mainmenu = Button("mainmenu", self.switch_scene, 50, 275, 150, 20, func_args=[TitleScene()])

    def gameovertextgen(self, string):
        text = []
        for i in string:
            text_render = self.font.render(i, 0, (0, 0, 0))
            text.append(text_render)
        return text

    def update(self, delta):
        self.player.update(delta)
        self.mainmenu.update()
        if self.level_scene.score > self.hs:
            self.data['high-score'] = self.level_scene.score
            with open("config.json", "w") as file:
                json.dump(self.data, file)

    def render(self, screen):
        self.level_scene.render(screen)
        self.mainmenu.render(screen)
        for i, j in enumerate(self.gameovertext):
            screen.blit(j, j.get_rect(center=(125, 125+25*i)))

    def process_input(self, events):
        self.mainmenu.process_input(events)
