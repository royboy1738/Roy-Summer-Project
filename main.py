"""
Starting Template

"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Example"
SPEED = 10


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color("barn.png")
        self.dancer = None
        self.move_sound = None

        self.dir_list = None

    def setup(self):
        self.dancer = arcade.Sprite("dancer.png", scale=0.1,
                                    center_x=400, center_y=400)
        self.move_sound = arcade.load_sound("audio/move.wav")

        self.up = arcade.Sprite("up.png", scale=0.1,
                                    center_x=200, center_y=200)

        self.down = arcade.Sprite("down.png", scale=0.1,
                                center_x=200, center_y=200)

        self.right = arcade.Sprite("right.png", scale=0.1,
                                center_x=200, center_y=200)

        self.left = arcade.Sprite("left.png", scale=0.1,
                                center_x=200, center_y=200)

    def on_draw(self):
        arcade.start_render()
        self.dancer.draw()

        # Messages
    def on_update(self, time):
        self.monkey.update()
        self.time += time

    def on_key_press(self, key, mod):
        if key == arcade.key.LEFT:
            self.dancer.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.dancer.change_x = +SPEED
        elif key == arcade.key.DOWN:
            self.dancer.change_y = -SPEED
        elif key == arcade.key.UP:
            self.dancer.change_y = +SPEED
            arcade.play_sound(self.move_sound)

    def on_key_release(self, key, mod):
        if key == arcade.key.LEFT:
            self.dancer.change_x = 0
        elif key == arcade.key.RIGHT:
            self.dancer.change_x = 0
        elif key == arcade.key.DOWN:
            self.dancer.change_y = 0
        elif key == arcade.key.UP:
            self.dancer.change_y = 0

def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
