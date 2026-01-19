from PyQt5.QtGui import QVector2D
from pygame import *
from pygame.math import *
from random import *

BLACK = (0,0,0)
CYAN = (0, 255, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
WIN_W = 700
WIN_H = 500
FPS = 100
X1, Y1 = 50 , 350
X2, Y2 = 625 , 300

UP = Vector2(0,-1)
DOWN = Vector2(0,1)
LEFT = Vector2(-1,0)
RIGHT = Vector2(1,0)

SRC = 'src/'
STOP_V = (0, 0)
CRUSADERS_SIZE = (100, 30)
SNITCH = (50, 50)

class WorkClass(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            (w, h)
        )
        self.position = Vector2(x,y)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rad_width = w // 2
        self.rad_height = h // 2

    def draw(self, widow):
        pos = self.position - Vector2(self.rad_width, self.rad_height)
        self.rect = Rect(pos - Vector2(), self.image.get_size())
        draw.rect(widow, CYAN, self.rect, 3)
        widow.blit(self.image,pos)

class NoGamePersona(WorkClass):
    def __init__(self, img, x, y, w, h, velocity):
        super().__init__(img, x, y, w, h)
        self.velocity = Vector2(velocity)
        self.direct = Vector2(UP)
        self.image_left = transform.flip(self.image,False,False)
        self.image_right = transform.flip(self.image,True,False)
        self.image_up = transform.rotate(self.image,-90)
        self.image_down = transform.rotate(self.image,90)
        self.image = self.image_up
        self.score = 0

    def move_up(self):
        if self.position[1] > 0:
            self.position = self.position + UP
            self.image = self.image_up
            self.velocity = UP
    def move_down(self):
        if self.position[1] < WIN_H:
            self.position = self.position + DOWN
            self.image = self.image_down
            self.velocity = DOWN
    def move_left(self):
        if self.position[0] > 0:
            self.position = self.position + LEFT
            self.image = self.image_left
            self.velocity = LEFT
    def move_right(self):
        if self.position[0] < WIN_W:
            self.position = self.position + RIGHT
            self.image = self.image_right
            self.velocity = RIGHT
    def rotate(self):
        rotored_img_size = Vector2(self.image.get_size())
        pos = self.position - rotored_img_size * 0.5
        self.rect = Rect(pos, rotored_img_size)
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

class Ball(WorkClass):
    def __init__(self, img, x, y, w, h, velocity):
        super().__init__(img, x, y, w, h)
        self.speed = velocity
        self.velocity = Vector2(choice((velocity,-velocity)),choice((velocity,-velocity)))
        self.angle = 1
        self.left_turn = self.velocity[0] < 0

    #аttorney = направление движения по часовой.
    def rotate(self, attorney):
        if not attorney :
            self.angle = -1
        else:
            self.angle = 1

    def move(self):
        self.position += self.velocity
        if 0 < self.position[0] < WIN_W and 0 < self.position[1] < WIN_H :
            self.position += self.velocity
        else:
            self.reset_ball()

    def draw(self, window):
        self.angle += 111
        rotored_img = transform.rotozoom(self.image, self.angle, 1.0)
        rotored_img_size = Vector2(rotored_img.get_size())
        pos = self.position - rotored_img_size * 0.5
        self.rect = Rect(pos, rotored_img_size)

        window.blit(rotored_img, pos)
    def reset_ball(self):
        self.position = Vector2(WIN_W // 2, WIN_H // 2)
        self.velocity = Vector2(choice((self.speed,-self.speed)),choice((self.speed,-self.speed)))

