import arcade
from pyglet.graphics import Batch

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class SetupView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.game_view = game_view

    def on_draw(self):
        self.clear()
        self.batch = Batch()
        start_text = arcade.Text("Jump Game", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                 arcade.color.WHITE, font_size=50, anchor_x="center", batch=self.batch)
        any_key_text = arcade.Text("Any key to start",
                                   self.window.width / 2, self.window.height / 2 - 75,
                                   arcade.color.GRAY, font_size=20, anchor_x="center", batch=self.batch)
        self.batch.draw()

    def on_key_press(self, key, modifiers):
        self.game_view.setup()
        self.window.show_view(self.game_view)