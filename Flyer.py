import pygame
import settings

class Flyer(pygame.sprite.Sprite):
    def __init__(self, groups, flyer_image):
        super().__init__(groups)

        #image
        self.image = pygame.image.load(flyer_image).convert_alpha()

        #rect
        self.rect = self.image.get_rect(midleft = (settings.WINDOW_WIDTH/20, settings.WINDOW_HEIGHT/2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        #movement
        self.gravity = 600
        self.direction = 0

        #mask
        self.mask = pygame.mask.from_surface(self.image)

    def apply_gravity (self, delta_time):
        self.direction += self.gravity * delta_time
        self.pos.y += self.direction * delta_time
        self.rect.y = round(self.pos.y)

    def move_up(self):
        self.direction = -400

    def update (self, delta_time):
        self.apply_gravity(delta_time)