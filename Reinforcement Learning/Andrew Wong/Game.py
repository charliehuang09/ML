import pygame
import time
import sys
from Stages import *
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
FPS = 60
COLLISION_TOLERANCE = 20
RED_LEFT = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/Andrew Wong/Assets/Red_Left.png')
RED_RIGHT = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/Andrew Wong/Assets/Red_Right.png')
BLUE_LEFT = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/Andrew Wong/Assets/Blue_Left.png')
BLUE_RIGHT = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/Andrew Wong/Assets/Blue_Right.png')
RED_LEFT = pygame.transform.scale(RED_LEFT, (90, 70))
RED_RIGHT = pygame.transform.scale(RED_RIGHT, (90, 70))
BLUE_LEFT = pygame.transform.scale(BLUE_LEFT, (90, 70))
BLUE_RIGHT = pygame.transform.scale(BLUE_RIGHT, (90, 70))
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill((255,255,255))
CLOCK = pygame.time.Clock()
pygame.display.update()
class Player:
    def __init__(self, right_img, left_img, x, y, gravity):
        self.right_img = right_img
        self.left_img = left_img
        self.rect = pygame.Rect(x, y, 100, 100)
        self.gun = "AK-47"
        self.ammo = 15
        self.xstrength = 1
        self.ystrength = -30
        self.xvelocity = 0
        self.yvelocity = 0
        self.gravity = gravity
    def jump(self):
        self.yvelocity += self.ystrength
    def right(self):
        self.xvelocity += self.xstrength
    def left(self):
        self.xvelocity -= self.xstrength
    def update(self):
        self.yvelocity *= 0.99
        self.yvelocity += self.gravity
        self.xvelocity *= 0.9
        self.rect.x += self.xvelocity
        self.rect.y += self.yvelocity
        if self.rect.y > 630:
            self.rect.y = 630
            self.yvelocity = 0
        if self.rect.x >= 1380:
            self.rect.x = 20
        elif self.rect.x <= 20:
            self.rect.x = 1380
    def draw(self):
        pygame.draw.rect(SCREEN, (0, 0, 0), (self.rect.x, self.rect.y, 100, 100))
        # SCREEN.blit(self.right_img, (self.rect.x, self.rect.y))
    def collide(self, obstacle):
        if self.rect.colliderect(obstacle.rect):
            if abs(self.rect.top - obstacle.rect.bottom) < COLLISION_TOLERANCE and self.yvelocity < 0:
                self.rect.top = obstacle.rect.bottom
                self.yvelocity = 0
                self.yvelocity *= -1
            if abs(self.rect.bottom - obstacle.rect.top) < COLLISION_TOLERANCE and self.yvelocity > 0:
                self.rect.bottom = obstacle.rect.top
                self.yvelocity = 0
                self.yvelocity *= -1
            if abs(self.rect.left - obstacle.rect.right) < COLLISION_TOLERANCE and self.xvelocity < 0:
                # self.rect.right = obstacle.rect.left
                # self.xvelocity = 0
                self.xvelocity *= -1
            if abs(self.rect.right - obstacle.rect.left) < COLLISION_TOLERANCE and self.xvelocity > 0:
                # self.rect.right = obstacle.rect.left
                # self.xvelocity = 0
                self.xvelocity *= -1
                
class Obstacle:
    def  __init__(self, x, y, x_size, y_size, R, G, B):
        self.rect = pygame.Rect(x, y, 100, 100)
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.R = R
        self.G = G
        self.B = B
    def draw(self):
        pygame.draw.rect(SCREEN, (self.R, self.G, self.B), (self.x, self.y, 100, 100))
def run():
    run = True
    player = Player(RED_LEFT, RED_RIGHT, 100, 100, 1)
    obstacles = empty()
    obstacles.append(Obstacle(0, 400, 100, 100, 100, 100, 100))#coords are top right corner
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill((255,255,255))
        pygame.draw.rect(SCREEN, (100, 100, 100), (0, 700, 1500, 20))
        player.update()
        for obstacle in obstacles:
            obstacle.draw()
            player.collide(obstacle)
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_a]:
            player.left()
        if userInput[pygame.K_d]:
            player.right()
        if userInput[pygame.K_w] and player.rect.y == 630:
            player.jump()
        player.draw()
        pygame.display.update()
run()
        

