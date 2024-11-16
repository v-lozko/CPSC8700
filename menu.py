import pygame
import settings

class Menu:
    def __init__(self, screen, options, title = None):
        self.screen = screen
        self.options = options
        self.title = title
        self.selected = 0
        self.font = pygame.font.Font('game_images/BD_Cartoon_Shout.ttf', 30)

    def menu(self):
        self.screen.fill((0, 0, 0))
        if self.title:
            title_text = self.font.render(self.title, True, (255, 255, 255))
            title_rect = title_text.get_rect(midtop = (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT*.25))
            self.screen.blit(title_text, title_rect)

        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected else (100, 100, 100)
            option_text = self.font.render(option, True, color)
            option_rect = option_text.get_rect(midtop = (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT*.5+ i * 50))
            self.screen.blit(option_text, option_rect)

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]
        return None


