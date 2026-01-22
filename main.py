import arcade

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from jump_game import JumpGame
from setup_view import SetupView


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    setup_view = SetupView(game_view=JumpGame())
    window.show_view(setup_view)
    arcade.run()

if __name__ == "__main__":
    main()