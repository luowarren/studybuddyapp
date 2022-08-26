import pygame

class SpriteSheet:
    def __init__(self, image, idx):
        self.image = image
        self.idx = idx

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), ((frame * width), (self.idx * height), (frame * width) + width, (self.idx * height) + height))
        image = pygame.transform.scale(image, (width * scale, height * scale))


        return image

class Animate:
    def __init__(self, steps, image_set, size=32, scale=10):
        self.steps = steps
        self.animation_list = []
        
        for x in range(len(steps)):
            self.animation_list.append(image_set.get_image(x, size, size, scale))

        