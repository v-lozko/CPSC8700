import pygame
import settings
from Score import Score
class Menu:
    def __init__(self, screen, options, title = None):
        self.screen = screen
        self.options = options
        self.title = title
        self.selected = 0
        self.font = pygame.font.Font('game_images/BD_Cartoon_Shout.ttf', 30)
        self.score = Score.get_instance()

    def menu(self):
        self.screen.fill((0, 0, 0))
        if self.title:
            title_text = self.font.render(self.title, True, (255, 255, 255))
            title_rect = title_text.get_rect(midtop = (settings.WINDOW_WIDTH/2, settings.WINDOW_HEIGHT*.25))
            self.screen.blit(title_text, title_rect)

            high_score_text = f"High Score: {self.score.get_high_score()}"
            prev_score_text = f"Previous Score: {self.score.get_prev_score()}"

            high_score_surf = self.font.render(high_score_text, True, (255, 255, 255))
            prev_score_surf = self.font.render(prev_score_text, True, (255, 255, 255))

            high_score_rect = high_score_surf.get_rect(midtop=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT * 0.35))
            prev_score_rect = prev_score_surf.get_rect(midtop=(settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT * 0.40))

            self.screen.blit(high_score_surf, high_score_rect)
            self.screen.blit(prev_score_surf, prev_score_rect)


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


