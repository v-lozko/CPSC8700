import pygame
import settings
from random import choice, randint

class Background(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        full_image = pygame.image.load('game_images/bg.png').convert()
        self.image = pygame.Surface((full_image.get_width()*2, full_image.get_height()))
        self.image.blit(full_image, (0, 0))
        self.image.blit(full_image, (full_image.get_width(),0))
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update (self, delta_time):
        self.pos.x -= 175* delta_time
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)

class Witch(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        #image
        self.image = pygame.image.load('game_images/witch_scaled.png').convert_alpha()

        #rect
        self.rect = self.image.get_rect(midleft = (settings.WINDOW_WIDTH/20, settings.WINDOW_HEIGHT/2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        #movement
        self.gravity = 600
        self.direction = 0

    def apply_gravity (self, delta_time):
        self.direction += self.gravity * delta_time
        self.pos.y += self.direction * delta_time
        self.rect.y = round(self.pos.y)

    def move_up(self):
        self.direction = -400


    def update (self, delta_time):
        self.apply_gravity(delta_time)
        #self.animate(delta_time)
        #self.rotate(delta_time)