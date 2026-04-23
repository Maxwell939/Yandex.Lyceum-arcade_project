import os
import sys
import arcade

from constants import PLAYER_SCALE, SCREEN_HEIGHT, RUN_SPEED


def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


BASE_PATH = get_base_path()


class PlayerHor(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()

        run_path = os.path.join(BASE_PATH, "textures", "player_hor", "img.png")  # пока пусть будет так

        self.texture = arcade.load_texture(run_path)

        self.center_x = x
        self.bottom = y
        self.scale = PLAYER_SCALE

        self.is_dead = False
        self.boost_active = False
        self.change_x = RUN_SPEED

    def update(self, delta_time: float = 1 / 60) -> None:
        super().update(delta_time)
        if self.top < 0 or self.bottom > SCREEN_HEIGHT:
            self.is_dead = True