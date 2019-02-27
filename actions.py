from main import game
from bullet import Bullet
import constants

ammo_list = pygame.sprite.Group()


if game.current_level.weapons:
    if len(game.ammo_list) < 6:
        constants.click_sound.play()
        bullet = Bullet()
        # Set the bullet so it is where the player is
        bullet.rect.x = game.player.rect.x
        bullet.rect.y = game.player.rect.y + 30
        # Add the bullet to the lists
        game.active_sprite_list.add(bullet)
        game.bullet_list.add(bullet)
        game.ammo_list.add(bullet)
    else:
        constants.out_of_bullets.play()
else:
    constants.out_of_bullets.play()