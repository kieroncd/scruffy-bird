from ui.button import Button


class TitleUI:

    def __init__(self):
        self.start = Button("start", self.switch_to_level, 50, 150, 150, 20)

    def update(self):
        self.start.update()

    def render(self, screen):
        self.start.render(screen)


