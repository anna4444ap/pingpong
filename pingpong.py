from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, height, width, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (height, width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")

racket1 = Player('snowman1.png', 30, 200, 50, 150, 4)
racket2 = Player('snowman2.png', 520, 200, 50, 150, 4)
ball = GameSprite('olaf.png', 200, 200, 50, 50, 4)
background = GameSprite('winter.jpg', 0, 0, win_width, win_height, 0)

game = True
finish = False
clock = time.Clock()
FPS = 60

win_player1 = GameSprite('player1.jpg', 0, 0, 0, win_width, win_height)
win_player2 = GameSprite('player2.jpg', 0, 0, 0, win_width, win_height)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= randint(-13, -7) / 10
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            fihish = True
            win_player2.reset()
            display.update()
            continue
        if ball.rect.x > win_width - 50:
            finish = True
            win_player1.reset()
            display.update()
            continue
        
        background.reset()

        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
