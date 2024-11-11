import pygame, sys, time
from sprites import Background, Witch, Obstacle
import settings


class Game:
    def __init__(self):
        pygame.init() #initializes all the pygame modules
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption('Tis The Seasons')
        self.clock = pygame.time.Clock()

        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        #sprite setup
        Background(self.all_sprites)
        self.witch = Witch(self.all_sprites)

        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

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
                        self.witch.move_up()
                if event.type == self.obstacle_timer:
                    Obstacle(self.all_sprites)


            #game logic
            self.all_sprites.update(delta_time)
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
            self.clock.tick(settings.FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()