'''
# 12.0 Jedi Training (10 pts)  Name:________________

Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!
'''

import arcade
SW = 600
SH = 600
SPEED_1 = 3
SPEED_2 = 4


class Box:
    def __init__(self, pos_x, pos_y, width, height, dx, dy, col, num):
        self.explosion = arcade.load_sound("explosion.wav")
        self.pluh = arcade.load_sound("laser.wav")
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
        self.col = col
        self.num = num

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)

    def update_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < self.width/2:
            self.pos_x = self.width/2
            if self.num == 1:
                arcade.play_sound(self.explosion,)
            else:
                arcade.play_sound(self.pluh)

        elif self.pos_x > SW - self.width/2:
            self.pos_x = SW - self.width/2
            if self.num == 1:
                arcade.play_sound(self.explosion,)
            else:
                arcade.play_sound(self.pluh)

        elif self.pos_y < self.width/2:
            self.pos_y = self.width/2
            if self.num == 1:
                arcade.play_sound(self.explosion,)
            else:
                arcade.play_sound(self.pluh)
        elif self.pos_y > SH - self.width/2:
            self.pos_y = SH - self.width/2
            if self.num == 1:
                arcade.play_sound(self.explosion,)
            else:
                arcade.play_sound(self.pluh)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.box = Box(100, 300, 30, 30, 0, 0, arcade.color.RED, 1)
        self.box_2 = Box(500, 300, 30, 30, 0, 0, arcade.color.BLUE, 0)
        self.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        self.box.draw_box()
        self.box_2.draw_box()

    def on_update(self, dt):
        self.box.update_box()
        self.box_2.update_box()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.box_2.dx = -SPEED_2
        elif key == arcade.key.RIGHT:
            self.box_2.dx = SPEED_2
        elif key == arcade.key.UP:
            self.box_2.dy = SPEED_2
        elif key == arcade.key.DOWN:
            self.box_2.dy = -SPEED_2

        elif key == arcade.key.A:
            self.box.dx = -SPEED_1
        elif key == arcade.key.D:
            self.box.dx = SPEED_1
        elif key == arcade.key.W:
            self.box.dy = SPEED_1
        elif key == arcade.key.S:
            self.box.dy = -SPEED_1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box_2.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.box_2.dy = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.box.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.box.dy = 0



def main():
    window = MyGame(SW, SH, "12.0 Jedi Training")
    arcade.run()

if __name__=="__main__":
    main()