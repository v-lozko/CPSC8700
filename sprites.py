from random import choice
from Background import Background
from Flyer import Flyer
from Obstacle import Obstacle

class SpriteFactory:
    holiday_sprites = {
        "Halloween": {
            "background": 'game_images/halloween_bg.png',
            "flyer": 'game_images/witch.png',
            "obstacle_bottom": 'game_images/halloween_tree.png',
            "obstacle_top": 'game_images/bats.png',
        },
        "Thanksgiving": {
            "background": 'game_images/thanksgiving_bg.png',
            "flyer": 'game_images/turkey.png',
            "obstacle_bottom": 'game_images/thanksgiving_tree.png',
            "obstacle_top": 'game_images/leaves.png',
        },
        "Christmas": {
            "background": 'game_images/christmas_bg.png',
            "flyer": 'game_images/santa.png',
            "obstacle_bottom": 'game_images/christmas_tree.png',
            "obstacle_top": 'game_images/snow.png',
        }
    }

    @staticmethod
    def create_background(groups, holiday):
        background_image = SpriteFactory.holiday_sprites[holiday]["background"]
        return Background(groups,background_image)

    @staticmethod
    def create_flyer(groups, holiday):
        flyer_image = SpriteFactory.holiday_sprites[holiday]["flyer"]
        return Flyer(groups,flyer_image)

    @staticmethod
    def create_obstacle(groups, holiday):
        obstacle_location = choice(('top', 'bottom'))
        obstacle_image = (
            SpriteFactory.holiday_sprites[holiday]["obstacle_top"]
            if obstacle_location == "top"
            else SpriteFactory.holiday_sprites[holiday]["obstacle_bottom"]
        )
        return Obstacle(groups, obstacle_image, obstacle_location)