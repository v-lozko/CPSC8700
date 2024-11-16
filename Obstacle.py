import pygame
import settings
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, obstacle_image, location):
        super().__init__(groups)
        x = settings.WINDOW_WIDTH + randint(100,200)
        self.image = pygame.image.load(obstacle_image).convert_alpha()
        if location == 'bottom':
            self.rect = self.image.get_rect(midbottom = (x, settings.WINDOW_HEIGHT) )
        else:
            y = randint(-50, -10)
            self.rect = self.image.get_rect(midtop = (x,y))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        #mask
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, delta_time):
        self.pos.x -= 400 * delta_time
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -20:
                self.kill()
