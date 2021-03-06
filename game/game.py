import pygame
import random
import sys
import os
import time
from record_and_cut.input_key_ctrl_micr import simulate_key_press, release_key, record_order

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_RETURN,
    K_r,
    K_1,
    K_2,
    K_3,
    KEYDOWN,
    QUIT,
)

pygame.init()

pygame.display.set_caption("Moonlanding with Speech Recognition")

# DEFINE WIDTH AND HIGHT
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650

# CREATE SCREEN OBJECT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font_a = pygame.font.Font('./game/data/consola.ttf', 36)
font_b = pygame.font.Font('./game/data/consola.ttf', 23)
clock = pygame.time.Clock()


def choose_player():
    """
    Lets you choose the rocket
    :return: Returns a boolean to see if the game shall terminate and 2 paths for the images
    """

    def resource_path(relative_path):
        """
        Creates the path to a picture for an object
        :param relative_path: Accepts the relative path for a picture
        :return: Returns the absolute path for a picture
        """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    # Load the player options
    rocket_01 = pygame.image.load(resource_path("game/data/naumannnofire.png"))
    rocket_02 = pygame.image.load(resource_path("game/data/studiforcenofire.png"))
    rocket_03 = pygame.image.load(resource_path("game/data/kuglernofire.png"))
    rocket_1 = pygame.transform.scale(rocket_01, (389, 403))
    rocket_2 = pygame.transform.scale(rocket_02, (389, 403))
    rocket_3 = pygame.transform.scale(rocket_03, (389, 403))
    # rocket_2 = rocket_1
    # rocket_3 = rocket_1

    start = True
    exit = False
    path = ""
    pathfire = ""
    pathflag_in = ""
    pathflag_out = ""
    difficulty = 0
    while start:
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    start = False
                    exit = True
                if event.key == K_1:
                    path = "game/data/naumannnofire.png"
                    pathfire = "game/data/naumannfire.png"
                    pathflag_in = "game/data/flag_heart_in.png"
                    pathflag_out = "game/data/flag_heart_out.png"
                    difficulty = 1
                    start = False
                if event.key == K_2:
                    path = "game/data/studiforcenofire.png"
                    pathfire = "game/data/studiforcefire.png"
                    pathflag_in = "game/data/flag_sf_in.png"
                    pathflag_out = "game/data/flag_sf_out.png"
                    difficulty = 2
                    start = False
                if event.key == K_3:
                    path = "game/data/kuglernofire.png"
                    pathfire = "game/data/kuglerfire.png"
                    pathflag_in = "game/data/flag_heart_in.png"
                    pathflag_out = "game/data/flag_heart_out.png"
                    difficulty = 3
                    start = False
            if event.type == QUIT:
                start = False
                exit = True

        screen.fill((0, 0, 0))
        choose = font_a.render("Choose your Player!", True, (255, 255, 255))
        choose_rect = choose.get_rect()
        screen.blit(choose, (SCREEN_WIDTH / 2 - choose_rect.right / 2, 50))

        screen.blit(rocket_1, (0, 100))
        screen.blit(rocket_2, (400, 100))
        screen.blit(rocket_3, (800, 100))
        choose1 = font_a.render("Press '1'", True, (255, 255, 255))
        screen.blit(choose1, (100, 500))
        choose2 = font_a.render("Press '2'", True, (255, 255, 255))
        screen.blit(choose2, (500, 500))
        choose3 = font_a.render("Press '3'", True, (255, 255, 255))
        screen.blit(choose3, (900, 500))
        pygame.display.flip()
        clock.tick(30)
    return exit, path, pathfire, difficulty, pathflag_in, pathflag_out


def menu():
    """
    Manages the Menu Screen
    :return: Returns a boolean to see if the game shall terminate
    """
    start = True
    space = True
    space_count = 0
    exit = False
    while start:
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:

                # ------------------------------------------------------------------------------------------------------
                """Integrating Speech Recognition"""
                if event.key == K_SPACE:
                    order = record_order()
                    if order == "go":
                        start = False
                    elif order == "stop":
                        start = False
                        exit = True

                # Was it the Escape key? If so, stop the loop.
                if event.key == K_RETURN:
                    start = False
                if event.key == K_ESCAPE:
                    start = False
                    exit = True

            if event.type == QUIT:
                start = False
                exit = True

        screen.fill((0, 0, 0))
        welcome = font_a.render("Welcome to Moonlanding!", True, (255, 255, 255))
        welcome_rect = welcome.get_rect()
        screen.blit(welcome, (SCREEN_WIDTH / 2 - welcome_rect.right / 2, 0))

        # Blinking Start Screen

        space_count += 1
        if space_count == 25:
            space = not space
            space_count = 0

        if space:
            space_press = font_a.render('!Press "Enter" or press "Space" and say "go" to start!', True, (255, 255, 255))
            space_press_rect = space_press.get_rect()
            screen.blit(space_press, (SCREEN_WIDTH / 2 - space_press_rect.right / 2, SCREEN_HEIGHT - 50))

        pygame.display.flip()
        clock.tick(20)
    return exit


def main(path, pathfire, difficulty, pathflag_in, pathflag_out):
    """
    Manages the actual game
    :return: A boolean to see if the game shall terminate and the message that shall be shown on the end screen
    :param: paths for the images (depending on the player's choice)
    """

    def resource_path(relative_path):
        """
        Creates the path to a picture for an object
        :param relative_path: Accepts the relative path for a picture
        :return: Returns the absolute path for a picture
        """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    class Player(pygame.sprite.Sprite):

        height = 500
        angle = 0
        angle_old = 0
        velocity = 0
        fuel = 200

        def __init__(self):
            super(Player, self).__init__()
            rocket_pic = resource_path(path)
            self.surf = pygame.transform.scale(pygame.image.load(rocket_pic).convert(), (130, 130))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()

        def angle_change(self, d):
            """
            Changes the angle of the rocket randomly
            :return: Returns the new angle
            """
            if d == 1:
                r = round(random.random() * 4)
                if r == 0:
                    self.angle -= 2
                elif r == 1:
                    self.angle -= 1
                elif r == 2:
                    pass
                elif r == 3:
                    self.angle += 1
                elif r == 4:
                    self.angle += 2
            elif d == 2:
                r = round(random.random() * 4)
                if r == 0:
                    self.angle -= 3
                elif r == 1:
                    self.angle -= 1
                elif r == 2:
                    pass
                elif r == 3:
                    self.angle += 2
                elif r == 4:
                    self.angle += 3
            else:
                r = round(random.random() * 4)
                if r == 0:
                    self.angle -= 3
                elif r == 1:
                    self.angle -= 3
                elif r == 2:
                    pass
                elif r == 3:
                    self.angle += 1
                elif r == 4:
                    self.angle += 4

        def rot_center(self, image, rect, angle):
            """
            rotates an image while keeping its center
            :param image: Accepts the image to be turned
            :param rect: Accepts the rect of said image
            :param angle: Accepts the angle for the turning
            :return: Returns a turned image
            """
            rot_image = pygame.transform.rotate(image, angle)
            rot_rect = rot_image.get_rect(center=rect.center)
            return rot_image, rot_rect

        def rotate(self, surface, rect, angle_old, angle):
            angle_new = angle_old - angle
            return self.rot_center(surface, rect, angle_new)

        def update(self, pressed_keys):
            """
            Updates the position and parameters of the rocket
            :param pressed_keys: Accepts a pressed key
            :return: Returns a boolean to set the fire animation
            """
            fire = False
            self.set_surf(pathfire)
            self.velocity += 5
            self.angle_old = self.angle
            self.angle_change(difficulty)
            if difficulty == 1:
                if pressed_keys[K_UP]:
                    self.velocity -= 12
                    fire = True
                    release_key("up")
                elif pressed_keys[K_DOWN]:
                    self.set_surf(path)
                    release_key("down")
                elif pressed_keys[K_LEFT]:
                    self.angle -= 2
                    fire = True
                    release_key("left")
                elif pressed_keys[K_RIGHT]:
                    self.angle += 2
                    fire = True
                    release_key("right")
            elif difficulty == 2:
                if pressed_keys[K_UP]:
                    self.velocity -= 10
                    fire = True
                    release_key("up")
                elif pressed_keys[K_DOWN]:
                    self.set_surf(path)
                    release_key("down")
                elif pressed_keys[K_LEFT]:
                    self.angle -= 2
                    fire = True
                    release_key("left")
                elif pressed_keys[K_RIGHT]:
                    self.angle += 2
                    fire = True
                    release_key("right")
            else:
                if pressed_keys[K_UP]:
                    self.velocity -= 8
                    fire = True
                    release_key("up")
                elif pressed_keys[K_DOWN]:
                    self.set_surf(path)
                    release_key("down")
                elif pressed_keys[K_LEFT]:
                    self.angle -= 2
                    fire = True
                    release_key("left")
                elif pressed_keys[K_RIGHT]:
                    self.angle += 2
                    fire = True
                    release_key("right")
            self.surf, self.rect = self.rot_center(self.surf, self.rect, -self.angle)
            self.height -= self.velocity
            self.rect.move_ip(0, self.velocity)
            # self.fuel -= 5
            # time.sleep(0.5)
            # self.set_surf("data/rocketup.png")
            return fire

        def get_height(self):
            """
            Returns the height of the rocket
            :return: Returns height as int
            """
            return self.height

        def get_velocity(self):
            """
            Returns velocity of rocket
            :return: Returns velocity as int
            """
            return self.velocity

        def get_angle(self):
            """
            Returns angle of rocket
            :return: Returns angle as int
            """
            return self.angle

        def get_fuel(self):
            """
            Returns left fuel of rocket
            :return: Returns fuel as int
            """
            return self.fuel

        def lower_fuel(self):
            """
            Lowers the fuel of the rocket
            :return: None
            """
            self.fuel -= 5

        def set_def(self):
            """
            Sets the default position of the rocket
            :return: None
            """
            self.rect.bottom = 150
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.right / 2

        def set_surf(self, path):
            """
            Sets the surface of the rocket
            :param path: Accepts a relative path to an image
            :return: None
            """
            rocket_pic = resource_path(path)
            self.surf = pygame.transform.scale(pygame.image.load(rocket_pic).convert(), (130, 130))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            # self.rect = self.surf.get_rect()

        def set_angle(self):
            """
            Sets the angle of the rocket
            :return: None
            """
            self.surf, self.rect = self.rot_center(self.surf, self.rect, -self.angle)

    class Meteor(pygame.sprite.Sprite):
        colision_steps = 0
        colision_height = 0

        def __init__(self):
            super(Meteor, self).__init__()
            rocket_pic = resource_path("game/data/meteor.png")
            self.surf = pygame.transform.scale(pygame.image.load(rocket_pic).convert(), (60, 60))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.colision_steps = random.randint(5, 15)
            self.colision_height = random.randint(100, 400)
            self.speed = 1

        def update(self):
            """
            Updates the position of the meteor
            :return: None
            """
            self.rect.move_ip(self.speed, 0)
            if self.rect.left > SCREEN_WIDTH:
                self.kill()

        def col_down(self):
            """
            Counts down the steps until the meteor appears
            :return: None
            """
            self.colision_steps -= 1

        def col_up(self):
            """
            Adds one step until collision
            :return: None
            """
            self.colision_steps += 1

        def get_steps(self):
            """
            Returns left steps until the meteor appears
            :return: Returns left steps as int
            """
            return self.colision_steps

        def get_height(self):
            """
            Returns the height where the meteor appears
            :return: Returns the height as int
            """
            return self.colision_height

        def set_def(self):
            """
            Sets the default position of the meteor
            :return: None
            """
            self.rect.top = SCREEN_HEIGHT - self.colision_height
            self.rect.right = 0

    class Moon(pygame.sprite.Sprite):
        def __init__(self):
            super(Moon, self).__init__()
            moon_pic = resource_path("game/data/moon.png")
            self.surf = pygame.transform.scale(pygame.image.load(moon_pic).convert(), (SCREEN_WIDTH, 100))
            self.rect = self.surf.get_rect()

        def set_def(self):
            """
            Sets default position of Moon
            :return: None
            """
            self.rect.bottom = SCREEN_HEIGHT
            self.rect.left = 0

    class Microphone(pygame.sprite.Sprite):
        def __init__(self):
            super(Microphone, self).__init__()
            mic_pic = resource_path("game/data/microphone.png")
            self.surf = pygame.transform.scale(pygame.image.load(mic_pic).convert(), (30, 30))
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()

        def set_on(self):
            self.rect.top = 70
            self.rect.left = 10

        def set_off(self):
            self.bottom = SCREEN_HEIGHT + 40
            self.rect.left = -40

    class Explosion(pygame.sprite.Sprite):
        def __init__(self):
            super(Explosion, self).__init__()

        def set_small(self, pos_bottom):
            explo_pic = resource_path("game/data/explo_small.png")
            self.surf = pygame.transform.scale(pygame.image.load(explo_pic).convert(), (300, 400))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.bottom = pos_bottom
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.right / 2

        def set_big(self, pos_bottom):
            explo_pic = resource_path("game/data/explo_big.png")
            self.surf = pygame.transform.scale(pygame.image.load(explo_pic).convert(), (300, 400))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.bottom = pos_bottom
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.right / 2

        def set_off(self):
            self.rect.top = SCREEN_HEIGHT

    class Flag(pygame.sprite.Sprite):
        def __init__(self):
            super(Flag, self).__init__()
            self.flag_in = resource_path(pathflag_in)
            self.flag_out = resource_path(pathflag_out)

        def set_in(self, pos_bottom):
            flag_pic = self.flag_in
            self.surf = pygame.transform.scale(pygame.image.load(flag_pic).convert(), (200, 300))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.bottom = SCREEN_HEIGHT + 10
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.right / 2 + 250

        def set_out(self, pos_bottom):
            flag_pic = self.flag_out
            self.surf = pygame.transform.scale(pygame.image.load(flag_pic).convert(), (200, 300))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.rect.bottom = SCREEN_HEIGHT + 10
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.right / 2 + 250

        def change_flag(self, flagin, flagout):
            self.flag_in = flagin
            self.flag_out = flagout

    rocket = Player()
    meteor = Meteor()
    moon = Moon()
    mic = Microphone()
    explosion = Explosion()
    flag = Flag()

    moon.set_def()
    rocket.set_def()
    meteor.set_def()
    mic.set_off()

    meteor_group = pygame.sprite.Group()
    meteor_group.add(meteor)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(moon)
    all_sprites.add(rocket)
    all_sprites.add(meteor)
    all_sprites.add(mic)

    status = "Quit voluntarily"

    running = True
    step = 0
    strike = False
    exit = False
    fire = False
    listen = False
    listen_time = 0
    order = ""
    crash = False
    meteordown = False
    said_go = False

    while running:

        if not fire:
            if not strike:
                waiting = True
                if step == 0:
                    waiting = False
                if listen:
                    waiting = False
                    order = record_order()
                    if order == "right":
                        simulate_key_press("right")
                    elif order == "left":
                        simulate_key_press("left")
                    elif order == "up":
                        simulate_key_press("up")
                    elif order == "down":
                        simulate_key_press("down")
                    elif order == "go":
                        simulate_key_press("down")
                        said_go = True
                    elif order == "stop":
                        running = False
                    listen = False
                    mic.set_off()
                while waiting:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            # --------------------------------------------------------------------------------------
                            """Integrating Speech Recognition"""
                            """-> after pressing space wave file is recorded, cutted and key press is simulated
                            TIP: while-loop recognizes key press simulation in next loop,then rocket object is
                            updated and after that the key is released"""
                            if event.key == K_SPACE:
                                mic.set_on()
                                listen = True
                                waiting = False
                                meteordown = False

                            if event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT or event.key == K_DOWN:
                                if event.key == K_UP:
                                    order = "up"
                                elif event.key == K_LEFT:
                                    order = "left"
                                elif event.key == K_RIGHT:
                                    order = "right"
                                else:
                                    if said_go:
                                        said_go = False
                                    else:
                                        order = "down"
                                pressed_keys = pygame.key.get_pressed()
                                fire = rocket.update(pressed_keys)
                                waiting = False
                                meteordown = True
                                if not event.key == K_DOWN:
                                    rocket.lower_fuel()
                                # print(fire)
                            if event.key == K_ESCAPE:
                                running = False
                                waiting = False
                        if event.type == QUIT:
                            running = False
                            waiting = False
                            exit = True

                try:
                    if meteordown:
                        meteor.col_down()
                except Exception:
                    pass

            if strike:
                meteor.update()
                if meteor.rect.left > SCREEN_WIDTH:
                    meteor = -1
                    strike = False
                    time.sleep(0.3)
                    rocket.set_surf(path)
                    rocket.set_angle()
                    # fire = False

            try:
                if meteor.get_steps() == 0:
                    strike = True
            except Exception:
                pass

            step = -1

            if pygame.sprite.spritecollideany(rocket, meteor_group):
                running = False
                status = "Rocket was hit"

        else:
            time.sleep(0.3)
            rocket.set_surf(path)
            rocket.set_angle()
            fire = False

        screen.fill((0, 0, 0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

            # Variablen
        velocity_val = rocket.get_velocity()
        height_val = rocket.get_height()
        angle_val = rocket.get_angle()
        fuel_val = rocket.get_fuel()
        try:
            meteor_height_val = meteor.get_height()
            meteor_step_val = meteor.get_steps()
        except Exception:
            meteor_height_val = "N/A"
            meteor_step_val = "N/A"

        # Schriftzug
        values = font_b.render("Velocity: " + str(velocity_val) + "   Height: " + str(height_val) + "   Angle: " + str(
            angle_val) + "   Step to Meteor: " + str(meteor_step_val) + "   Meteor height: " + str(
            meteor_height_val) + "   Fuel: " + str(fuel_val),
                               True, (255, 255, 255))
        values_rect = values.get_rect()

        screen.blit(values, values_rect)
        last_order = font_b.render("Last Order: " + order, True, (255, 100, 0))
        last_order_rect = last_order.get_rect()
        screen.blit(last_order, (0, 40))

        if height_val <= 0:
            running = False
            if velocity_val >= 10 or angle_val <= -6 or angle_val >= 6:
                status = "Crash"
            else:
                status = "Landed successfully"
        if fuel_val <= -5:
            running = False
            status = "Out of fuel"

        pygame.display.flip()
        # clock.tick(30)

    # Explosion simulation
    if status == "Crash" or status == "Rocket was hit":
        explo = True
        if status == "Crash":
            height = SCREEN_HEIGHT
        else:
            height = SCREEN_HEIGHT - meteor.get_height() + 60
        explosion.set_small(height)
        crash_sprites = pygame.sprite.Group()
        crash_sprites.add(moon)
        crash_sprites.add(explosion)
        runs = 0
        while explo:
            if runs == 8:
                explosion.set_big(height)
            elif runs == 16:
                explosion.set_small(height)
            elif runs == 24:
                explosion.set_off()
            elif runs == 36:
                explo = False
            runs += 1
            screen.fill((0, 0, 0))
            for entity in crash_sprites:
                screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
            clock.tick(30)

    # Flag simulation
    rocket_destroyed = False
    if status == "Crash" or status == "Rocket was hit":
        flag.change_flag("game/data/flag_shit_in.png", "game/data/flag_shit_out.png")
        rocket_destroyed = True
    elif status == "Out of fuel":
        flag.change_flag("game/data/flag_shit_in.png", "game/data/flag_shit_out.png")
    elif status == "Quit voluntarily":
        flag.change_flag("game/data/flag_sloth_in.png", "game/data/flag_sloth_out.png")

    flag_bool = True
    height = SCREEN_HEIGHT
    flag.set_in(height)
    landing_sprites = pygame.sprite.Group()
    landing_sprites.add(moon)
    if not rocket_destroyed:
        landing_sprites.add(rocket)
    landing_sprites.add(flag)
    runs = 0
    while flag_bool:
        if runs == 8:
            flag.set_out(height)
        elif runs == 16:
            flag.set_in(height)
        elif runs == 24:
            flag.set_out(height)
        elif runs == 32:
            flag.set_in(height)
        elif runs == 40:
            flag.set_out(height)
        elif runs == 48:
            flag.set_in(height)
        elif runs == 56:
            flag.set_out(height)
        elif runs == 64:
            flag_bool = False
        runs += 1
        screen.fill((0, 0, 0))
        for entity in landing_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()
        clock.tick(30)

    return exit, status


def end_screen(status):
    """
    Manages the end screen
    :param status: Accepts the message that shall be shown on the end screen
    :return: Returns a boolean to see if the game shall terminate
    """
    game_over = True
    exit = False
    while game_over:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # ------------------------------------------------------------------------------------------------------
                """Integrating SR"""
                if event.key == K_SPACE:

                    order = record_order()
                    if order == "yes":
                        game_over = False
                    elif order == "no" or order == "stop":
                        game_over = False
                        exit = True

                if event.key == K_r:
                    game_over = False
                if event.key == K_ESCAPE:
                    game_over = False
                    exit = True
                    # release_key("escape")
            elif event.type == QUIT:
                game_over = False
                exit = True

        screen.fill((0, 0, 0))

        again = font_a.render("Do you want to restart the game?", True, (255, 255, 255))
        again_rect = again.get_rect()
        screen.blit(again,
                    (SCREEN_WIDTH / 2 - again_rect.right / 2, (SCREEN_HEIGHT / 3) * 2 - 70 - again_rect.bottom / 2))

        # --------------------------------------------------------------------------------------------------------------
        """Adding Tips for User Interaction"""
        tip = font_a.render('(If yes press R or say "yes")', True, (10, 255, 10))
        tip_rect = tip.get_rect()
        screen.blit(tip, (SCREEN_WIDTH / 2 - tip_rect.right / 2, (SCREEN_HEIGHT / 3) * 2 - tip_rect.bottom / 2))
        tip2 = font_a.render('(If no press ESC or say "no")', True, (255, 10, 10))
        tip2_rect = tip2.get_rect()

        screen.blit(tip2, (SCREEN_WIDTH / 2 - tip2_rect.right / 2, (SCREEN_HEIGHT / 3) * 2 + 50 - tip2_rect.bottom / 2))
        state = font_a.render(str(status), True, (255, 255, 255))
        status_rect = state.get_rect()
        screen.blit(state, (SCREEN_WIDTH / 2 - status_rect.right / 2, (SCREEN_HEIGHT / 3) - status_rect.bottom / 2))
        pygame.display.flip()
    return exit


def game():
    """
    Manages the order of the menu, the actual game and the end screen
    :return: None
    """
    while True:
        quit, path, pathfire, difficulty, pathflag_in, pathflag_out = choose_player()
        if quit:
            pygame.quit()
            break
        quit = menu()
        if quit:
            pygame.quit()
            break
        quit, status = main(path, pathfire, difficulty, pathflag_in, pathflag_out)
        if quit:
            pygame.quit()
            break
        quit = end_screen(status)
        if quit:
            pygame.quit()
            break
