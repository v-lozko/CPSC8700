import pygame
import settings
import sys


class waiting_screen:
    def __init__(self, screen, holiday):
        self.screen = screen
        self.holiday = holiday
        if holiday == "Halloween":
            self.full_image = pygame.image.load('game_images/halloween_bg.png').convert()
        elif holiday == "Thanksgiving":
            self.full_image = pygame.image.load('game_images/thanksgiving_bg.png').convert()
        elif holiday == "Christmas":
            self.full_image = pygame.image.load('game_images/christmas_bg.png').convert()
        self.font = pygame.font.Font('game_images/BD_Cartoon_Shout.ttf', 20)

    def display(self):
        self.screen.blit(self.full_image, (0, 0))
        text = self.font.render(self.holiday, True, (255, 255, 255))
        rect = text.get_rect(midtop=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))
        self.screen.blit(text, rect)
        pygame.display.update()

    def waiting(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False