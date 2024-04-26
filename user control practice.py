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


Starter Testing Code:
'''
import arcade
SW = 600
SH = 600
SPEED = 5



class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.explosion = arcade.load_sound("pluh.wav")
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

        joysticks = arcade.get_joysticks()

        if joysticks:
            # Grab the first one in  the list
            self.joystick = joysticks[0]

            # Open it for input
            self.joystick.open()

            # Push this object as a handler for joystick events.
            # Required for the on_joy* events to be called.
            self.joystick.push_handlers(self)
        else:
            # Handle if there are no joysticks.
            print("There are no joysticks, plug in a joystick and run again.")
            self.joystick = None

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_ball(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < self.rad:
            # self.pos_x += SPEED
            self.pos_x = self.rad
            arcade.play_sound(self.explosion,)

        elif self.pos_x > SW - self.rad:
            # self.pos_x -= SPEED
            self.pos_x = SW - self.rad
            arcade.play_sound(self.explosion)

        elif self.pos_y < self.rad:
            # self.pos_y += SPEED
            self.pos_y = self.rad
            arcade.play_sound(self.explosion)
        elif self.pos_y > SH - self.rad:
            # self.pos_y -= SPEED
            self.pos_y = SH - self.rad
            arcade.play_sound(self.explosion)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball = Ball(320, 240, 0, 0, 15, arcade.color.AUBURN)
        self.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_mouse_press(self, x, y, button, modifiers):
        pass
        # if button == arcade.MOUSE_BUTTON_LEFT:
        #     print("Left mouse button pressed at", x, y)
        # elif button == arcade.MOUSE_BUTTON_RIGHT:
        #     print("Right mouse button pressed at", x, y)

    def on_mouse_motion(self, x, y, dx, dy):
        pass
        # self.ball.pos_x = x
        # self.ball.pos_y = y

    def on_update(self, dt):
        self.ball.update_ball()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED
        elif key == arcade.key.UP:
            self.ball.dy = SPEED
        elif key == arcade.key.DOWN:
            self.ball.dy = -SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0


def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()

if __name__=="__main__":
    main()
