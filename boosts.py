import arcade
import sys
import os
from constants import JUMP_SPEED
from player import Player
def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

BASE_PATH = get_base_path()

class Boost(arcade.Sprite):
    def __init__(self):
        super().__init__()
    def update(self, player: arcade.Sprite, delta_time: float = 1 / 60):
        super().update(delta_time)
        if self.collides_with_sprite(player) and player.change_y < 0:
            player.change_y = JUMP_SPEED * self.boost_strength
            if player.change_y > 0:
                player.boost_active = True
class Spring(Boost):
    def __init__(self):
        super().__init__()
        string_path = os.path.join(BASE_PATH, "textures", "boosts", "spring", "spring1.png")
        self.textures = []
        self.textures.append(arcade.load_texture(string_path))
        self.scale = 1.5
        self.boost_strength = 2