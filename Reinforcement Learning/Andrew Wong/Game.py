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
bullets = []
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
class Bullet:
    def __init__(self, x, y, direction, damage, speed, R, G, B):
        self.rect = pygame.Rect(x, y, 25, 10)
        self.timer = 50
        self.R = R
        self.G = G
        self.B = B
        self.direction = direction
        self.speed = speed
        self.damage = damage
    def draw(self):
        self.timer -= 1
        self.rect.x += self.direction * self.speed
        if self.rect.x >= 1380:
            self.rect.x = 0
        elif self.rect.x <= 0:
            self.rect.x = 1380
        pygame.draw.rect(SCREEN, (self.R, self.G, self.B), (self.rect.x, self.rect.y, 25, 10))
class ak47:
    def __init__(self):
        self.ammo = 15
        self.maxAmmo = 15
        self.currCooldown = 0
        self.cooldown = 30
        self.damage = 20
    def shoot(self, x, y, direction, R, G, B):
        if self.currCooldown > 0:
            return
        global bullets
        self.ammo -= 1
        bullets.append(Bullet(x + 50, y + 30, direction, 10, 25, R, G, B))
        self.currCooldown = self.cooldown
        print(self.ammo)
class smg:
    def __init__(self):
        self.ammo = 30
        self.maxAmmo = 30
        self.currCooldown = 0
        self.cooldown = 5
        self.damage = 0.1
    def shoot(self, x, y, direction, R, G, B):
        if self.currCooldown > 0:
            return
        global bullets
        self.ammo -= 1
        bullets.append(Bullet(x + 50, y + 30, direction, 10, 25, R, G, B))
        self.currCooldown = self.cooldown
    

class Player:
    def __init__(self, right_img, left_img, x, y, gravity, direction, startImg, guns, R, G, B):
        self.right_img = right_img
        self.left_img = left_img
        self.rect = pygame.Rect(x, y, right_img.get_width(), right_img.get_height())
        self.xstrength = 1
        self.ystrength = -30
        self.xvelocity = 0
        self.yvelocity = 0
        self.gravity = gravity
        self.canJump = False
        self.currimg = startImg
        self.direction = direction
        self.health = 100
        self.guns = guns
        self.gun_id = 0
        self.R = R
        self.G = G
        self.B = B
        self.timer = 0
    def jump(self):
        self.yvelocity += self.ystrength
        self.canJump = False
    def right(self):
        self.xvelocity += self.xstrength
    def left(self):
        self.xvelocity -= self.xstrength
    def shoot(self):
        if self.timer > 0 or self.guns[self.gun_id].ammo <= 0:
            return
        self.guns[self.gun_id].shoot(self.rect.x, self.rect.y, self.direction, self.R, self.G, self.B)
    def changeGun(self):
        self.gun_id += 1
        self.gun_id %= len(self.guns)
        print(self.gun_id)
    def reload(self):
        if self.timer > 0:
            return
        self.guns[self.gun_id].ammo = self.guns[self.gun_id].maxAmmo
        self.timer = 120
    def update(self):
        self.timer -= 1
        for gun in self.guns:
            gun.currCooldown -= 1
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
        if abs(self.xvelocity) > 1:
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
        SCREEN.blit(self.currimg, (self.rect.x, self.rect.y))
        pygame.draw.rect(SCREEN, (0, 255, 0), (self.rect.x, self.rect.y - 20, self.health, 10))
        pygame.draw.rect(SCREEN, (0, 0, 255), (self.rect.x, self.rect.y - 40, (100 / self.guns[self.gun_id].maxAmmo) * self.guns[self.gun_id].ammo, 10))
        if self.timer > 0:
            if self.direction == 1:
                pygame.draw.rect(SCREEN, (0, 255, 0), (self.rect.x + 30, self.rect.y + 20, 10, 10))
            else:
                pygame.draw.rect(SCREEN, (0, 255, 0), (self.rect.x + 50, self.rect.y + 20, 10, 10))
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
    global bullets
    bullets = []
    run = True
    redGuns = []
    blueGuns = []
    redGuns.append(ak47())
    redGuns.append(smg())
    blueGuns.append(ak47())
    blueGuns.append(smg())
    redPlayer = Player(RED_LEFT, RED_RIGHT, 90, 70, 1, 1, RED_RIGHT, redGuns, 255, 0, 0)
    bluePlayer = Player(BLUE_LEFT, BLUE_RIGHT, 1310, 70, 1, -1, BLUE_LEFT, blueGuns, 0, 0, 255)
    obstacles = threeBlocks()
    redReload = False
    blueReload = False
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

        if userInput[pygame.K_a]:
            redPlayer.left()
        if userInput[pygame.K_d]:
            redPlayer.right()
        if userInput[pygame.K_w] and redPlayer.rect.y == 630:
            redPlayer.jump()
        if userInput[pygame.K_w] and redPlayer.canJump:
            redPlayer.jump()
        if userInput[pygame.K_s]:
            redPlayer.shoot()
        if userInput[pygame.K_r]:
            redPlayer.reload()
        if userInput[pygame.K_q] and not redReload:
            redReload = True
            redPlayer.changeGun()
        elif not userInput[pygame.K_q]:
            redReload = False
            
        if userInput[pygame.K_LEFT]:
            bluePlayer.left()
        if userInput[pygame.K_RIGHT]:
            bluePlayer.right()
        if userInput[pygame.K_UP] and bluePlayer.rect.y == 630:
            bluePlayer.jump()
        if userInput[pygame.K_UP] and bluePlayer.canJump:
            bluePlayer.jump()
        if userInput[pygame.K_DOWN]:
            bluePlayer.shoot()
        if userInput[pygame.K_l]:
            bluePlayer.reload()
        if userInput[pygame.K_m] and not blueReload:
            blueReload = True
            bluePlayer.changeGun()
        elif not userInput[pygame.K_m]:
            blueReload = False

        redPlayer.update()
        redPlayer.draw()
        bluePlayer.update()
        bluePlayer.draw()
        for bullet in bullets:
            bullet.draw()
            if bullet.timer <= 0:
                bullets.remove(bullet)
                continue
            if bullet.R == 255 and bullet.rect.colliderect(bluePlayer):
                bluePlayer.health -= bullet.damage
                bullets.remove(bullet)
                continue
            if bullet.R == 0 and bullet.rect.colliderect(redPlayer):
                redPlayer.health -= bullet.damage
                bullets.remove(bullet)
                continue
        if redPlayer.health <= 0:
            SCREEN.fill((255, 255, 255))
            bluePlayer.draw()
            pygame.display.update()
            time.sleep(2)
            return
        if bluePlayer.health <= 0:
            SCREEN.fill((255, 255, 255))
            redPlayer.draw()
            pygame.display.update()
            time.sleep(2)
            return
        pygame.display.update()
        # print(redPlayer.health, bluePlayer.health)
run()