
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


class Ball(Game_sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed_x = self.speed
        self.speed_y = self.speed

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y >= 450 or self.rect.y <= 0:
            self.speed_y *= -1
        if sprite.collide_rect(self, right_rocket) or sprite.collide_rect(self, left_rocket):
            self.speed_x *= -1



font.init()
font_1 = font.Font(None, 50)
wintext_1 = font_1.render('PLAYER 1 WIN!', True, (255, 255, 0))
winrect = wintext_1.get_rect()
wintext_2 = font_1.render('PLAYER 2 WIN!', True, (255, 255, 0))
ball = Ball('tenis_ball.png', 325, 225, 3, 50, 50)

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
        ball.update()
        ball.draw()
        if ball.rect.x <= 0:
            final = True
            main.blit(wintext_2, (350-winrect.width/2, 250-winrect.height/2))
        elif ball.rect.x >= 650:
            final = True
            main.blit(wintext_1, (350-winrect.width/2, 250-winrect.height/2))



    display.update()
    clock.tick(60)
