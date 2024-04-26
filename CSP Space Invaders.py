import arcade
import random

SW = 640
SH = 480
SPEED = 10


class Stars:
    def __init__(self, pos_x, pos_y, rad, dy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.dy = dy

    def draw_star(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, arcade.color.WHITE, 0, 40)

    def update_star(self):
        self.pos_y -= self.dy

        if self.pos_y < self.rad:
            self.pos_y = random.randint(SH, SH*2)
            self.pos_x = random.randint(0, SW)

            self.rad = random.randint(1, 3)


class Ship:
    def __init__(self, pos_x, pos_y, width, height, dx):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.dx = dx

    def draw_ship(self):
        arcade.draw_arc_filled(self.pos_x, self.pos_y, 50, 50, arcade.color.GREEN, -180, 0)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y + 7, self.width - 20, self.height - 35, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y + 16,self.width - 40, self.height - 45, arcade.color.YELLOW)

    def update_ship(self):
        self.pos_x += self.dx

        if self.pos_x >= 625:
            self.pos_x = -25
        elif self.pos_x <= -25:
            self.pos_x = 625


class Bullet:
    def __init__(self, pos_x, pos_y, rad, dy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.dy = dy

    def draw_bullet(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, arcade.color.RED)

    def update_bullet(self):
        self.pos_y += self.dy

        if self.pos_y > SH:
            self.dy = 0
            self.pos_y = -10
            self.pos_x = 320


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.ship = Ship(320, 30, 50, 50, 0)

        self.laser = arcade.load_sound("laser.wav")

        self.star_list = []
        self.bullet_list = []

        for i in range(300):
            x = random.randint(0, SW)
            y = random.randint(0, SH+100)
            dy = 1
            rad = random.randint(1, 3)
            self.star = Stars(x, y, rad, dy)
            self.star_list.append(self.star)

    def on_draw(self):
        arcade.start_render()
        for bullet in self.bullet_list:
            bullet.draw_bullet()

        for star in self.star_list:
            star.draw_star()

        self.ship.draw_ship()

    def on_update(self, dt):
        for star in self.star_list:
            star.update_star()

        for bullet in self.bullet_list:
            bullet.update_bullet()

        self.ship.update_ship()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ship.dx = -SPEED
        elif key == arcade.key.RIGHT:
            self.ship.dx = SPEED

        if key == arcade.key.SPACE:
            bullet = Bullet(self.ship.pos_x, self.ship.pos_y, 2, 10)
            self.bullet_list.append(bullet)
            arcade.play_sound(self.laser)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ship.dx = 0
        elif key == arcade.key.RIGHT:
            self.ship.dx = 0


def main():
    window = MyGame(SW, SH, "CSP SPACE INVADERS!")
    arcade.run()


if __name__=="__main__":
    main()


