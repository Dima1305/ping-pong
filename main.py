
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
    def __init__(self, down, up, *args):
        super().__init__(*args)
        self.down = down
        self.up = up

    def update(self):
        pressed_b = key.get_pressed()
        if pressed_b[self.down] and self.rect.y < 400:
            self.rect.y += self.speed
        if pressed_b[self.up] and self.rect.y > 0:
            self.rect.y -= self.speed


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

right_rocket = Player(K_DOWN, K_UP, 'racket.png', 660, 200, 3, 20, 100)
left_rocket = Player(K_s, K_w, 'racket.png', 20, 200, 3, 20, 100)

game = True
final = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if final != True:
        main.blit(background, (0, 0))
        right_rocket.update()
        right_rocket.draw()
        left_rocket.update()
        left_rocket.draw()


    display.update()
    clock.tick(60)