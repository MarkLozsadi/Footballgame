import pygame

class TextLabel(pygame.sprite.Sprite):
    def __init__(self, fontType, fontSize , pos, color=(255,255,255), initial_value=""):
        super().__init__()
        self.font = pygame.font.SysFont(fontType, fontSize)
        self.color = color
        self.value = None
        # we need two Sprite attributes:
        #   .image is the Surface to blit
        #   .rect  is its position
        self.image = None
        self.rect = pygame.Rect(pos, (0,0))

        # set initial text (this will also set image & rect.size)
        self.set(initial_value)
        self.initialText = initial_value

    def set(self, new_value):
        """Update the displayed text (re-renders only on change)."""
        text = str(new_value)
        if text != self.value:
            self.value = text
            self.image = self.font.render(text, True, self.color)
            # update rect size, keeping the same topleft
            self.rect.size = self.image.get_size()

    def update(self, *args):
        """
        If you want to automatically change the label over time,
        you can override update here (e.g. to show a timer).
        Otherwise, leave it empty so Group.update() won’t break.
        """
        pass