import pygame
import settings
from random import choice, randint

from settings import WINDOW_WIDTH, WINDOW_HEIGHT


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

        #mask
        self.mask = pygame.mask.from_surface(self.image)

    def apply_gravity (self, delta_time):
        self.direction += self.gravity * delta_time
        self.pos.y += self.direction * delta_time
        self.rect.y = round(self.pos.y)

    def move_up(self):
        self.direction = -400

    #isn't working properly for some reason
    #def rotate(self):
        #rotated_witch = pygame.transform.rotozoom(self.image.copy(),-self.direction*0.0006,1)
       # self.image = rotated_witch
        #self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))


    def update (self, delta_time):
        self.apply_gravity(delta_time)
        #self.rotate()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        orientation = choice(('up', 'down'))

        x = WINDOW_WIDTH + randint(100,200)
        if orientation == 'up':
            self.image = pygame.image.load('game_images/tree.png').convert_alpha()
            y = WINDOW_HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom = (x, WINDOW_HEIGHT) )
        else:
            self.image = pygame.image.load('game_images/bats.png').convert_alpha()
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
