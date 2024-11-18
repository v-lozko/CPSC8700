import pygame, sys, time
from sprites import SpriteFactory
import settings
import menu
from Score import Score

score = Score.get_instance()
class Game:
    def __init__(self):
        score.reset_score()
        pygame.init() #initializes all the pygame modules
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption('Flying Through the Holidays')
        self.clock = pygame.time.Clock()
        self.active = True

        #game state
        self.game_state = "main_menu"
        self.selected_mode = None

        self.factory = SpriteFactory()

        self.background = None
        self.flyer = None
        self.score = 0
        self.active = False

        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        #text
        self.font = pygame.font.Font('game_images/BD_Cartoon_Shout.ttf',30)
        self.score = 0
        self.start_offset = 0

        #menu
        self.main_menu = menu.Menu(
            self.display_surface,
            ["Halloween", "Thanksgiving", "Christmas"],
            title = "Fly Through The Holidays"
        )

    def menu_selection(self, event):
        selected_mode = self.main_menu.input(event)
        if selected_mode:
            self.start_game(selected_mode)

    def start_game(self, holiday):
        self.game_state = "game"
        self.selected_mode = holiday
        self.active = True
        score.reset_score()
        self.score = score.get_score()
        self.thanks_switch = False
        self.christmas_switch = False

        self.all_sprites.empty()
        self.collision_sprites.empty()

        self.background = self.factory.create_background(self.all_sprites, holiday)
        self.flyer = self.factory.create_flyer(self.all_sprites, holiday)

        self.start_offset = pygame.time.get_ticks()

    def collisions(self):
        if pygame.sprite.spritecollide(self.flyer, self.collision_sprites, False,pygame.sprite.collide_mask)\
                or self.flyer.rect.bottom > settings.WINDOW_HEIGHT or  self.flyer.rect.bottom < 0:
            for sprite in self.collision_sprites.sprites():
                sprite.kill()
            self.active = False
            score.reset_score()
            self.score = score.get_score()
            self.game_state = "main_menu"
            self.start_offset = pygame.time.get_ticks()

    def display_score(self):
        if self.active:
            score.set_score((pygame.time.get_ticks()-self.start_offset)//100)
            self.score = score.get_score()
            y = settings.WINDOW_HEIGHT/10
        else:
            y = settings.WINDOW_HEIGHT*.75

        score_surf = self.font.render(str(self.score), True, 'black')
        score_rect = score_surf.get_rect(midtop = (settings.WINDOW_WIDTH/2, y))
        self.display_surface.blit(score_surf, score_rect)

    def run(self):
        last_time = time.time()
        while True:
            delta_time = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.game_state == "main_menu":
                    self.menu_selection(event)
                elif self.game_state == "game":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.active:
                        self.flyer.move_up()
                    if event.type == self.obstacle_timer and self.active:
                        self.factory.create_obstacle([self.all_sprites, self.collision_sprites],self.selected_mode)
                    if score.get_score() >= 300 and not self.thanks_switch:
                        self.thanks_switch = True
                        self.holiday = "Thanksgiving"
                        self.selected_mode = "Thanksgiving"
                        for sprite in self.collision_sprites.sprites():
                            sprite.kill()
                        self.background = self.factory.create_background(self.all_sprites, self.holiday)
                        self.flyer = self.factory.create_flyer(self.all_sprites, self.holiday)
                    if score.get_score() >= 600 and not self.christmas_switch:
                        self.christmas_switch = True
                        self.holiday = "Christmas"
                        self.selected_mode = "Christmas"
                        for sprite in self.collision_sprites.sprites():
                            sprite.kill()
                        self.background = self.factory.create_background(self.all_sprites, self.holiday)
                        self.flyer = self.factory.create_flyer(self.all_sprites, self.holiday)


            #game logic
            if self.game_state == "main_menu":
                self.main_menu.menu()
            elif self.game_state == "game":
                self.all_sprites.update(delta_time)
                self.collisions()
                self.all_sprites.draw(self.display_surface)
                self.display_score()
            pygame.display.update()
            self.clock.tick(settings.FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()