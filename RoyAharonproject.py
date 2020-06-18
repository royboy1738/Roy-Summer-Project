import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Example"
SPEED = 10


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.dancer = None
        self.up = None
        self.background = None
        self.move_sound = None
        self.initial = 0
        self.direction = 'up'
        self.total_time = 0.0
        self.points = 0

    def setup(self):
        self.dancer = arcade.Sprite("images/dancer.png", scale=0.45,
                                    center_x=400, center_y=400)
        self.move_sound = arcade.load_sound("audio/move.wav")

        self.stop = arcade.Sprite("images/stop.png", scale=0.1,
                                  center_x=400, center_y=400)
        self.total_time = 0.0

        self.background = arcade.load_texture("images/barn.jpg")


    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.dancer.draw()

        minutes = int(self.total_time) // 60

        seconds = int(self.total_time) % 60

        if seconds >= 35:
            self.stop.draw()

        final = f"Points: {str(self.points)}"
        arcade.draw_text(final, 325, 0, arcade.color.RED, 30)

        output = f"Time: {minutes:02d}:{seconds:02d}"

        arcade.draw_text(output, 300, 50, arcade.color.RED, 30)

    def on_update(self, time):
        self.dancer.update()

        if self.total_time <= 35:
            self.total_time += time

    def arrow_print(self):

        i = random.randint(0, 3)
        if i == 0:
            print('up')
            self.direction = 'up'
        elif i == 1:
           print('down')
           self.direction = 'down'
        elif i == 2:
            print('right')
            self.direction = 'right'
        elif i == 3:
            print('left')
            self.direction = 'left'

    def on_key_press(self, key, mod):
        if key == arcade.key.LEFT:
            if self.direction != 'left':
                print('WRONG')
                self.points -= 1
            if self.direction == 'left':
                self.points += 1
            self.arrow_print()
            self.dancer.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            if self.direction != 'right':
                print('WRONG')
                self.points -= 1
            if self.direction == 'right':
                self.points += 1
            self.arrow_print()
            self.dancer.change_x = +SPEED
        elif key == arcade.key.DOWN:
            if self.direction != 'down':
                print('WRONG')
                self.points -= 1
            if self.direction == 'down':
                self.points += 1
            self.arrow_print()
            self.dancer.change_y = -SPEED
        elif key == arcade.key.UP:
            if self.direction != 'up':
                print('WRONG')
                self.points -= 1
            if self.direction == 'up':
                self.points += 1
            self.arrow_print()
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
    print('up')
    arcade.run()

if __name__ == '__main__':
    main()