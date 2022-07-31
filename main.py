import pygame
from scene import TitleScene


def run_game():
    pygame.init()
    pygame.display.set_caption("Scruffy Bird: Pro")
    screen = pygame.display.set_mode((250, 300))
    clock = pygame.time.Clock()
    scene = TitleScene()

    while scene is not None:
        fil_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene.kill()
            else:
                fil_events.append(event)
        delta = clock.tick(60)
        screen.fill((0, 0, 0))
        scene.process_input(fil_events)
        scene.update(delta)
        scene.render(screen)
        scene = scene.next
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    run_game()
