import os
import sys
import arcade

from constants import PLAYER_SCALE, RUN_SPEED, HORIZONTAL_SCREEN_WIDTH, HORIZONTAL_SCREEN_HEIGHT


def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


BASE_PATH = get_base_path()


class PlayerHor(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()

        for i in range(12):
            self.textures.append(arcade.load_texture(os.path.join(BASE_PATH, "textures", "player", f"run{i}.png")))

        self.center_x = x
        self.bottom = y
        self.scale = PLAYER_SCALE
        self.cur_texture_index = 0
        self.texture = self.textures[self.cur_texture_index]
        self.texture_change_time = 0
        self.texture_change_delay = 0.05

        self.is_dead = False
        self.boost_active = False
        self.change_x = RUN_SPEED

    def update(self, delta_time: float = 1 / 60) -> None:
        super().update(delta_time)
        if self.top < 0:
            self.is_dead = True

        if self.left <= 0:
            self.left = 0
        elif self.right >= HORIZONTAL_SCREEN_WIDTH:
            self.right = HORIZONTAL_SCREEN_WIDTH

    def update_animation(self, delta_time: float = 1 / 60) -> None:
        self.texture_change_time += delta_time
        if self.texture_change_time >= self.texture_change_delay:
            self.texture_change_time -= self.texture_change_delay
            self.cur_texture_index = (self.cur_texture_index + 1) % len(self.textures)
            self.texture = self.textures[self.cur_texture_index]
