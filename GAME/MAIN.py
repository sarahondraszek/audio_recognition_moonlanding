import pygame
import random
import sys
import os

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_r,
    KEYDOWN,
    QUIT,
)

pygame.init()

pygame.display.set_caption("Moonlanding")

# DEFINE WIDTH AND HIGHT
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# CREATE SCREEN OBJECT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font_a = pygame.font.Font('data/consola.ttf', 36)
font_b = pygame.font.Font('data/consola.ttf', 25)
clock = pygame.time.Clock()


def menu():
    start = True
    space = True
    space_count = 0
    while start:
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_SPACE:
                    start = False

        screen.fill((0, 0, 0))
        welcome = font_a.render("Welcome to Moonlanding", True, (255, 255, 255))
        welcome_rect = welcome.get_rect()
        screen.blit(welcome, (SCREEN_WIDTH / 2 - welcome_rect.right / 2, 0))

        # Blinking 'Press Space'

        space_count += 1
        if space_count == 25:
            space = not space
            space_count = 0

        if space:
            space_press = font_a.render("!Press 'Space' to start!", True, (255, 255, 255))
            space_press_rect = space_press.get_rect()
            screen.blit(space_press, (SCREEN_WIDTH / 2 - space_press_rect.right / 2, SCREEN_HEIGHT - 50))

        pygame.display.flip()
        clock.tick(30)


def main():
    def resource_path(relative_path):
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

        def __init__(self):
            super(Player, self).__init__()
            rocket_pic = resource_path("data/rocketup.png")
            self.surf = pygame.transform.scale(pygame.image.load(rocket_pic).convert(), (60, 100))
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()

        def angle_change(self):
            r = round(random.random() * 4)
            if r == 0:
                self.angle -= 4
            elif r == 1:
                self.angle -= 2
            elif r == 2:
                pass
            elif r == 3:
                self.angle += 2
            elif r == 4:
                self.angle += 4

        def rot_center(self, image, rect, angle):
            """rotate an image while keeping its center"""
            rot_image = pygame.transform.rotate(image, angle)
            rot_rect = rot_image.get_rect(center=self.rect.center)
            return rot_image, rot_rect

        def rotate(self, surface, rect, angle_old, angle):
            angle_new = angle - angle_old
            return self.rot_center(surface, rect, angle_new)

        def update(self, pressed_keys):
            self.velocity += 5
            self.angle_old = self.angle
            self.angle_change()
            if pressed_keys[K_UP]:
                self.velocity -= 7
                # print("YES")
            if pressed_keys[K_LEFT]:
                self.angle -= 2
            elif pressed_keys[K_RIGHT]:
                self.angle += 2
            self.surf, self.rect = self.rotate(self.surf, self.rect, self.angle_old, self.angle)
            self.height -= self.velocity
            self.rect.move_ip(0, self.velocity)

        def get_height(self):
            return self.height

        def get_velocity(self):
            return self.velocity

        def get_angle(self):
            return self.angle

        def set_def(self):
            self.rect.top = 50
            self.rect.left = SCREEN_WIDTH / 2 - self.rect.right / 2

    class Meteor(pygame.sprite.Sprite):
        colision_steps = 0
        colision_height = 0

        def __init__(self):
            super(Meteor, self).__init__()
            rocket_pic = resource_path("data/meteor.png")
            self.surf = pygame.transform.scale(pygame.image.load(rocket_pic).convert(), (60, 60))
            self.rect = self.surf.get_rect()
            self.colision_steps = round(random.random() * 15)
            self.colision_height = round(random.random() * 300)
            self.speed = 20

        def update(self):
            self.rect.move_ip(self.speed, 0)
            if self.rect.left > SCREEN_WIDTH:
                self.kill()
                print("RAUS")

        def col_down(self):
            self.colision_steps -= 1

        def get_steps(self):
            return self.colision_steps

        def get_height(self):
            return self.colision_height

        def set_def(self):
            self.rect.top = SCREEN_HEIGHT - self.colision_height
            self.rect.right = 0

    class Moon(pygame.sprite.Sprite):
        def __init__(self):
            super(Moon, self).__init__()
            moon_pic = resource_path("data/moon.png")
            self.surf = pygame.transform.scale(pygame.image.load(moon_pic).convert(), (SCREEN_WIDTH, 100))
            self.rect = self.surf.get_rect()

        def set_def(self):
            self.rect.bottom = SCREEN_HEIGHT
            self.rect.left = 0

    rocket = Player()
    meteor = Meteor()
    moon = Moon()

    moon.set_def()
    rocket.set_def()
    meteor.set_def()

    meteor_group = pygame.sprite.Group()
    meteor_group.add(meteor)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(moon)
    all_sprites.add(rocket)
    all_sprites.add(meteor)

    running = True
    game_over = False
    step = 0
    strike = False
    flight = True

    while running:
        if not strike:
            waiting = True
            if step == 0:
                waiting = False
            while waiting:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT or event.key == K_DOWN:
                            pressed_keys = pygame.key.get_pressed()
                            rocket.update(pressed_keys)
                            waiting = False
                        if event.key == K_ESCAPE:
                            running = False
                            waiting = False

                    if event.type == QUIT:
                        running = False
                        waiting = False

            try:
                meteor.col_down()
            except Exception:
                pass

        if strike:
            meteor.update()
            if meteor.rect.left > SCREEN_WIDTH:
                meteor = -1
                strike = False

        try:
            if meteor.get_steps() == 0:
                strike = True
        except Exception:
            pass

        step = -1

        if pygame.sprite.spritecollideany(rocket, meteor_group):
            running = False
            print("Getroffen")



        screen.fill((0, 0, 0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Variablen
        velocity_val = rocket.get_velocity()
        height_val = rocket.get_height()
        angle_val = rocket.get_angle()
        try:
            meteor_height_val = meteor.get_height()
            meteor_step_val = meteor.get_steps()
        except Exception:
            meteor_height_val = "N/A"
            meteor_step_val = "N/A"

        # Schriftzug
        values = font_b.render("Velocity: " + str(velocity_val) + "   Height: " + str(height_val) + "   Angle: " + str(
            angle_val) + "   Step to Meteor: " + str(meteor_step_val) + "   Meteor height: " + str(meteor_height_val),
                               True, (255, 255, 255))
        values_rect = values.get_rect()

        screen.blit(values, values_rect)

        if height_val <= 0:
            running = False
            if velocity_val >= 10 or angle_val <= -6 or angle_val >= 6:
                print("Absturz")
            else:
                print("Landung erfolgreich")

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def end_screen():
    game_over = True
    exit = False
    while game_over:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_r:
                    game_over = False
                if event.key == K_ESCAPE:
                    game_over = False
                    exit = True
            elif event.type == QUIT:
                game_over = True

        screen.fill((0, 0, 0))

        again = font_b.render("Press 'R' to restart the game", True, (255, 255, 255))
        again_rect = again.get_rect()
        screen.blit(again, (SCREEN_WIDTH / 2 - again_rect.right / 2, 10))
    #return exit

def game():
    menu()
    main()
    #end_screen()

game()
