import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, groups, background_image):
        super().__init__(groups)
        full_image = pygame.image.load(background_image).convert()
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