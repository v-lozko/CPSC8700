from random import choice
from Background import Background
from Flyer import Flyer
from Obstacle import Obstacle

class SpriteFactory:
    def __init__(self):
        self.holiday_sprites = {
            "Halloween": {
                "background": 'game_images/thanksgiving.png',
                "flyer": 'game_images/turkey_scaled.png',
                "obstacle_top": 'game_images/tg_tree3.png',
                "obstacle_bottom": 'game_images/bats.png',
            },
            "Thanksgiving": {
                "background": 'game_images/thanksgiving.png',
                "flyer": 'game_images/turkey_scaled.png',
                "obstacle_top": 'game_images/tg_tree3.png',
                "obstacle_bottom": 'game_images/bats.png',
            },
            "Christmas": {
                "background": 'game_images/thanksgiving.png',
                "flyer": 'game_images/turkey_scaled.png',
                "obstacle_top": 'game_images/tg_tree3.png',
                "obstacle_bottom": 'game_images/bats.png',
            }
        }

    def create_background(self, groups, holiday):
        background_image = self.holiday_sprites[holiday]["background"]
        return Background(groups,background_image)

    def create_flyer(self, groups, holiday):
        flyer_image = self.holiday_sprites[holiday]["flyer"]
        return Flyer(groups,flyer_image)

    def create_obstacle(self, groups, holiday):
        obstacle_location = choice(('top', 'bottom'))
        obstacle_image = (
            self.holiday_sprites[holiday]["obstacle_top"]
            if obstacle_location == "top"
            else self.holiday_sprites[holiday]["obstacle_bottom"]
        )
        return Obstacle(groups, obstacle_image, obstacle_location)