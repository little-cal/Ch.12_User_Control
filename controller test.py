import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.05


class Player:
    def __init__(self, pos_x, pos_y, width, height, dx, dy, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
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
            print(joysticks)
        else:
            # Handle if there are no joysticks.
            print("There are no joysticks, plug in a joystick and run again.")
            self.joystick = None

    def draw_player(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)

    def update(self):
        """ Move the player """

        # If there is a joystick, grab the speed.
        if self.joystick:

            # x-axis
            self.dx = self.joystick.x * MOVEMENT_SPEED
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.dx) < DEAD_ZONE:
                self.dx = 0

            # y-axis
            self.dy = -self.joystick.y * MOVEMENT_SPEED
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.dy) < DEAD_ZONE:
                self.dy = 0

        # Move the player
        self.pos_x += self.dx
        self.pos_y += self.dy

        # Keep from moving off-screen
        if self.pos_x < self.width / 2:
            self.pos_x = self.width / 2

        if self.pos_x > SCREEN_WIDTH - self.width / 2:
            self.pos_x = SCREEN_WIDTH - self.width / 2

        if self.pos_y < self.width / 2:
            self.pos_y = self.width / 2

        if self.pos_y > SCREEN_HEIGHT - self.width / 2:
            self.pos_y = SCREEN_HEIGHT - self.width / 2

    # noinspection PyMethodMayBeStatic
    def on_joybutton_press(self, _joystick, button):
        """ Handle button-down event for the joystick """
        print("Button {} down".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joybutton_release(self, _joystick, button):
        """ Handle button-up event for the joystick """
        print("Button {} up".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        """ Handle hat events """
        print("Hat ({}, {})".format(hat_x, hat_y))


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.player = Player(300, 300, 30, 30, 0, 0, arcade.color.RED)
        self.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        self.player.draw_player()

    def on_update(self, dt):
        self.player.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player.dy = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.dy = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.dx = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.dx = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.dy = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.dx = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Controller Testing")
    arcade.run()


if __name__ == "__main__":
    main()