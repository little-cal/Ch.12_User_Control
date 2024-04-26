'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.

'''
import arcade
import random
import time

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

        elif self.pos_x > SCREEN_WIDTH - self.width / 2:
            self.pos_x = SCREEN_WIDTH - self.width / 2

        elif self.pos_y < self.width / 2:
            self.pos_y = self.width / 2

        elif self.pos_y > SCREEN_HEIGHT - self.width / 2:
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


class Projectile:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_projectile(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_projectile(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_x < self.rad or self.pos_x > SCREEN_WIDTH - self.rad:
            self.dx *= -1

        elif self.pos_y < self.rad or self.pos_y > SCREEN_HEIGHT - self.rad:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.player = Player(300, 30, 30, 30, 0, 0, arcade.color.RED)
        self.set_mouse_visible(True)

        # self.rad1 = self.player.pos_x + self.player.width/2
        # self.rad2 = self.rad1 + 1
        # self.rad3 = self.player.pos_x - self.player.width/2
        # self.rad4 = self.rad3 - 1
        #
        # self.rad5 = self.player.pos_y + self.player.width / 2
        # self.rad6 = self.rad5 + 1
        # self.rad7 = self.player.pos_y - self.player.width / 2
        # self.rad8 = self.rad7 - 1

        self.clock = 0

        self.projectile_list = []

        # self.x1 = 30
        # self.y1 = 30
        #
        # self.x2 = 60
        # self.y2 = 570
        #
        # self.x3 = 30
        # self.y3 = 120
        #
        # self.x4 = 570
        # self.y4 = 90

        # for i in range(10):
        #     dy = random.randint(-2, 2)
        #     while dy == 0:
        #         dy = random.randint(-2, 2)
        #     self.projectile = Projectile(self.x1, self.y1, 0, dy, 10, arcade.color.BLUE)
        #     self.projectile_list.append(self.projectile)
        #     if self.x1 < 600:
        #         self.x1 += 60
        #
        # for i in range(9):
        #     dy = random.randint(-2, 2)
        #     while dy == 0:
        #         dy = random.randint(-2, 2)
        #     self.projectile = Projectile(self.x2, self.y2, 0, dy, 10, arcade.color.BLUE)
        #     self.projectile_list.append(self.projectile)
        #     if self.x2 < 600:
        #         self.x2 += 60
        #
        # for i in range(7):
        #     dx = random.randint(-4, 4) + random.random()
        #     while dx == 0:
        #         dx = random.randint(-4, 4) + random.random()
        #     self.projectile = Projectile(self.x3, self.y3, dx, 0, 10, arcade.color.BLUE)
        #     self.projectile_list.append(self.projectile)
        #     if self.y3 < 600:
        #         self.y3 += 60
        #
        # for i in range(8):
        #     dx = random.randint(-4, 4) + random.random()
        #     while dx == 0:
        #         dx = random.randint(-4, 4) + random.random()
        #     self.projectile = Projectile(self.x4, self.y4, dx, 0, 10, arcade.color.BLUE)
        #     self.projectile_list.append(self.projectile)
        #     if self.y4 < 600:
        #         self.y4 += 60

    def on_draw(self):
        arcade.start_render()
        self.player.draw_player()
        for projectile in self.projectile_list:
            projectile.draw_projectile()

    def on_update(self, dt):
        self.player.update()
        self.clock += dt
        if self.clock > 3:
            for projectile in self.projectile_list:
                projectile.update_projectile()

        # if self.projectile.pos_x - self.projectile.rad >= self.rad1 and self.projectile.pos_x <= self.rad2:
        #     time.sleep(0.01)
        # elif self.projectile.pos_x + self.projectile.rad <= self.rad3 and self.projectile.pos_x >= self.rad4:
        #     time.sleep(0.01)
        # elif self.projectile.pos_y - self.projectile.rad >= self.rad5 and self.projectile.pos_y <= self.rad6:
        #     time.sleep(0.01)
        # elif self.projectile.pos_y + self.projectile.rad <= self.rad7 and self.projectile.pos_y >= self.rad8:
        #     time.sleep(0.01)

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
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "User Control Project")
    arcade.run()


if __name__ == "__main__":
    main()