from pygame import *
from random import randint

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# clase del jugador principal
class Player(GameSprite):
    pass
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed      
    
class Enemy(GameSprite):
    side = 'up'
    def update(self):
        global lost
        if self.rect.y <= 0:
            self.side = 'down'
        if self.rect.y >= win_width -85:
            self.side = 'up'
        if self.side == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed  

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('pin pong con ignacio')
background = transform.scale(image.load('tralalero-tralala.jpg'),(win_width, win_height))

palo1 = Player('racket.png',5, win_height - 100,80,100,10)
bola = Enemy('tenis_ball.png',5, win_width - 80, 40, 80 ,50)
palo2 = Player('racket.png',5, win_height - 100, 80,100,10)

game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    
    palo1.update()
    bola.update()
    palo2.update()

    window.blit(background,(0,0))

    display.update()
    clock.tick(FPS)    
