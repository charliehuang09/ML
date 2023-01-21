import pygame
import time
import sys
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
FPS = 60
COLLISION_TOLERANCE = 30
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
class Bullet:
    def __init__(self, x, y, direction, R = 255, G = 0, B = 0):
        self.rect = pygame.Rect(x, y, 25, 10)
        self.timer = 50
        self.R = R
        self.G = G
        self.B = B
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 25
    def draw(self):
        self.timer -= 1
        self.rect.x += self.direction * self.speed
        if self.rect.x >= 1380:
            self.rect.x = 0
        elif self.rect.x <= 0:
            self.rect.x = 1380
        pygame.draw.rect(SCREEN, (self.R, self.G, self.B), (self.rect.x, self.rect.y, 25, 10))

class Player:
    def __init__(self, right_img, left_img, x, y, gravity, direction):
        self.right_img = right_img
        self.left_img = left_img
        self.rect = pygame.Rect(x, y, right_img.get_width(), right_img.get_height())
        self.xstrength = 1
        self.ystrength = -30
        self.xvelocity = 0
        self.yvelocity = 0
        self.gravity = gravity
        self.canJump = False
        self.currimg = self.left_img
        self.direction = direction
        self.gunCooldown = 10
        self.cooldown = 0
    def jump(self):
        self.yvelocity += self.ystrength
    def right(self):
        self.xvelocity += self.xstrength
    def left(self):
        self.xvelocity -= self.xstrength
    def update(self):
        self.cooldown -= 1
        if self.xvelocity < 0:
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.right_img.get_width(), self.right_img.get_height())
            self.currimg = self.right_img
            self.direction = -1
        if self.xvelocity > 0:
            self.rect = pygame.Rect(self.rect.x, self.rect.y, self.left_img.get_width(), self.left_img.get_height())
            self.currimg = self.left_img
            self.direction = 1
        self.yvelocity *= 0.99
        self.yvelocity += self.gravity
        self.xvelocity *= 0.9
        self.rect.x += self.xvelocity
        self.rect.y += self.yvelocity
        if self.rect.y > 630:
            self.rect.y = 630
            self.yvelocity = 0
        if self.rect.x >= 1380:
            self.rect.x = 0
        elif self.rect.x <= 0:
            self.rect.x = 1380
    def draw(self):
        # pygame.draw.rect(SCREEN, (0, 0, 0), (self.rect.x, self.rect.y, 100, 100))
        SCREEN.blit(self.currimg, (self.rect.x, self.rect.y))
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
                self.canJump = True
            if abs(self.rect.left - obstacle.rect.right) < COLLISION_TOLERANCE and self.xvelocity < 0:
                # self.rect.left = obstacle.rect.right
                self.xvelocity = -1
                # self.xvelocity *= -1
            if abs(self.rect.right - obstacle.rect.left) < COLLISION_TOLERANCE and self.xvelocity > 0:
                # self.rect.right = obdstacle.rect.left
                self.xvelocity = 1
                # self.xvelocity *= -1

class Obstacle:
    def  __init__(self, x, y, x_size, y_size, R = 100, G = 100, B = 100):
        self.rect = pygame.Rect(x, y, x_size, y_size)
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.R = R
        self.G = G
        self.B = B
    def draw(self):
        pygame.draw.rect(SCREEN, (self.R, self.G, self.B), (self.x, self.y, self.x_size, self.y_size))
def empty():
    return []
def threeBlocks():#800, 1400, x, y
    obstacles = []
    obstacles.append(Obstacle(0, 150, 200, 50))
    obstacles.append(Obstacle(1200, 150, 200, 50))
    obstacles.append(Obstacle(650, 500, 90, 70))
    obstacles.append(Obstacle(350, 300, 90, 70))
    obstacles.append(Obstacle(950, 300, 90, 70))
    return obstacles
def run():
    run = True
    redPlayer = Player(RED_LEFT, RED_RIGHT, 90, 70, 1, 1)
    bluePlayer = Player(BLUE_LEFT, BLUE_RIGHT, 1310, 70, 1, -1)
    obstacles = threeBlocks()
    bullets = []
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill((255,255,255))
        pygame.draw.rect(SCREEN, (100, 100, 100), (0, 700, 1500, 20))
        redPlayer.canJump = False
        for obstacle in obstacles:
            obstacle.draw()
            redPlayer.collide(obstacle)
            bluePlayer.collide(obstacle)
        userInput = pygame.key.get_pressed()

        if userInput[pygame.K_s] and redPlayer.cooldown <= 0:
            bullets.append(Bullet(redPlayer.rect.x + 50, redPlayer.rect.y + 30, redPlayer.direction))
            redPlayer.cooldown = redPlayer.gunCooldown
        if userInput[pygame.K_a]:
            redPlayer.left()
        if userInput[pygame.K_d]:
            redPlayer.right()
        if userInput[pygame.K_w] and redPlayer.rect.y == 630:
            redPlayer.jump()
            redPlayer.canJump = False
        if userInput[pygame.K_w] and redPlayer.canJump:
            redPlayer.jump()
            redPlayer.canJump = False
        if userInput[pygame.K_s] and redPlayer.cooldown <= 0:
            bullets.append(Bullet(redPlayer.rect.x + 50, redPlayer.rect.y + 30, redPlayer.direction))
            redPlayer.cooldown = redPlayer.gunCooldown
        print(redPlayer.xvelocity)
            
        if userInput[pygame.K_LEFT]:
            bluePlayer.left()
        if userInput[pygame.K_RIGHT]:
            bluePlayer.right()
        if userInput[pygame.K_UP] and bluePlayer.rect.y == 630:
            bluePlayer.jump()
            bluePlayer.canJump = False
        if userInput[pygame.K_UP] and bluePlayer.canJump:
            bluePlayer.jump()
            bluePlayer.canJump = False
        if userInput[pygame.K_DOWN] and bluePlayer.cooldown <= 0:
            bullets.append(Bullet(bluePlayer.rect.x + 50, bluePlayer.rect.y + 30, bluePlayer.direction))
            bluePlayer.cooldown = bluePlayer.gunCooldown
        redPlayer.update()
        redPlayer.draw()
        bluePlayer.update()
        bluePlayer.draw()
        for bullet in bullets:
            bullet.draw()
            if bullet.timer <= 0:
                bullets.remove(bullet)
        pygame.display.update()
run()