import pygame, sys, time
from sprites import Background, Witch, Obstacle
import settings


class Game:
    def __init__(self):
        pygame.init() #initializes all t he pygame modules
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption('Tis The Seasons')
        self.clock = pygame.time.Clock()
        self.active = True

        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        #sprite setup
        Background(self.all_sprites)
        self.witch = Witch(self.all_sprites)

        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        #text
        self.font = pygame.font.Font('game_images/BD_Cartoon_Shout.ttf',30)
        self.score = 0
        self.start_offset = 0

        #menu
        self.menu_surf = pygame.image.load('game_images/menu.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(topleft=(0,0))

    def collisions(self):
        if pygame.sprite.spritecollide(self.witch, self.collision_sprites, False,pygame.sprite.collide_mask)\
                or self.witch.rect.bottom > settings.WINDOW_HEIGHT or  self.witch.rect.bottom < 0:
            for sprite  in self.collision_sprites.sprites():
                sprite.kill()
            self.active = False


    def display_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks()-self.start_offset)//100
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.active:
                            self.witch.move_up()
                        else:
                            self.witch = Witch(self.all_sprites)
                            self.active = True
                            self.start_offset = pygame.time.get_ticks()
                if event.type == self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprites])


            #game logic
            self.all_sprites.update(delta_time)
            self.collisions()
            self.all_sprites.draw(self.display_surface)


            if self.active:
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf, self.menu_rect)
            self.display_score()
            pygame.display.update()
            self.clock.tick(settings.FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()