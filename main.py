import pygame
from scene.titlescene import TitleScene

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((250, 300))
    clock = pygame.time.Clock()
    scene = TitleScene()
    running = True

    while scene is not None:
        fil_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene.switch_scene(None)
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
