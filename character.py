import pygame

class Buddy(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()
        #Config
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

            # Draw
        pygame.draw.rect(self.image, color , [0, 0, width, height])

        # Fetch
        self.rect = self.image.get_rect()

    def right(self, pixels):
        self.rect.x += pixels
    def left(self, pixels):
        self.rect.x -= pixels
    def up(self, pixels):
        self.rect.y -= pixels
    def down(self, pixels):
        self.rect.y += pixels