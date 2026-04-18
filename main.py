import arcade
import sys
import game_view
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from game_view import GameView, GameViewHorizontal
from score_manager import ScoreManager
from start_view import StartView


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    setup_view = StartView(game_view=GameView(), score_manager=ScoreManager())
    window.show_view(setup_view)
    arcade.run()
if __name__ == "__main__":
    main()