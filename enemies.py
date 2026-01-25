import arcade


class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__()

    def update(self, player, delta_time: float = 1 / 60) -> None:
        super().update(delta_time)
        if self.collides_with_sprite(player):
            self.kill()