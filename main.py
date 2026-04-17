
from pygame import *

main = display.set_mode((700, 500))
display.set_caption('пинг-понг')

background = transform.scale(image.load('ping-pong picture.jpg'), (700, 500))


clock = time.Clock()


class Game_sprite(sprite.Sprite):
    def __init__(self, picture_name, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(picture_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        main.blit(self.image, (self.rect.x, self.rect.y))


class Player(Game_sprite):
    def update(self):
        pressed_b = key.get_pressed()
        if pressed_b[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if pressed_b[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(Game_sprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.x = randint(0, 625)
            self.rect.y = -50
            global miss_score
            miss_score += 1



font.init()
font_1 = font.Font(None, 25)
wintext = font_1.render('YOU WIN!', True, (255, 255, 0))

game = True
final = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if final != True:
        main.blit(background, (0, 0))


    display.update()
    clock.tick(60)