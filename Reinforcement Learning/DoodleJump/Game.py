import pygame
import time
import sys
import random
import neat
pygame.init()
CLOCK = pygame.time.Clock()

SCREEN_HEIGHT = 1200
SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill((255,255,255))
pygame.display.update()
config_path = '/Users/charlie/ML/Reinforcement Learning/DoodleJump/config.txt'

CHARECTER = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/DoodleJump/Assets/Charecter.jpeg')
CHARECTER = pygame.transform.scale(CHARECTER, (64, 64))
GREEN_OBSTACLE = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/DoodleJump/Assets/Green_Obstacle.png')
GREEN_OBSTACLE = pygame.transform.scale(GREEN_OBSTACLE, (128, 32))

class Player:
    X_POS = 500
    Y_POS = 1000
    JUMP_VEL = 8.5

    def __init__(self, img):
        self.img = img
        self.xStrength = 1.5
        self.yStrength = 30
        self.xVelocity = 0
        self.yVelocity = -20
        self.gravity = 1
        self.y_limit = 400
        self.x_min = -50
        self.x_max = 50
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
    
    def update(self, speed):
        offset = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.left()
        if keys[pygame.K_d]:
            self.right()
        if keys[pygame.K_w]:
            self.jump()
        self.xVelocity *= 0.95
        self.yVelocity *= 0.99
        self.yVelocity += self.gravity
        self.xVelocity = max(self.xVelocity, self.x_min)
        self.xVelocity = min(self.xVelocity, self.x_max)
        self.X_POS += self.xVelocity
        self.Y_POS += self.yVelocity - speed
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.draw()
        return offset
    
    def jump(self):
        if self.yVelocity > 0:
            self.yVelocity = -self.yStrength
    
    def left(self):
        self.xVelocity = min(0, self.xVelocity)
        self.xVelocity -= self.xStrength
    
    def right(self):
        self.xVelocity = max(0, self.xVelocity)
        self.xVelocity += self.xStrength

    def draw(self):
        SCREEN.blit(self.img, (self.rect.x, self.rect.y))

class Obstacle:
    def __init__(self, img, x, y):
        self.img = img
        self.rect = pygame.Rect(x, y, img.get_width(), img.get_height())

    def draw(self, offset):
        self.rect.y -= offset
        SCREEN.blit(self.img, (self.rect.x, self.rect.y))
        return self.rect.y > 1200



player = Player(CHARECTER)
obstacles = []
obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 1100))
obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 900))
obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 700))
obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 500))#6
obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 300))
obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 100))
score = 0
speed = -0.1
while(True):
    SCREEN.fill((255,255,255))
    player.update(speed)

    for obstacle in obstacles:
        done = obstacle.draw(speed)
        if player.rect.colliderect(obstacle.rect):
            player.jump()
        if (done):
            obstacles.remove(obstacle)
            obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 0))
            score += 1
    pygame.display.update()
    speed -= 0.001
    CLOCK.tick(60)


# def eval_genomes(genomes, config):
#     global game_speed, x_pos_bg, y_pos_bg, obstacles, players, ge, nets, points
#     obstacles = []
#     players = []
#     ge = []
#     nets = []
#     score = 0
#     game_speed = 20

#     for genome_id, genome in genomes:
#         players.append(player(CHARECTER))
#         ge.append(genome)
#         net = neat.nn.FeedForwardNetwork.create(genome, config)
#         nets.append(net)
#         genome.fitness = 0

#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         SCREEN.fill((255,255,255))
#         for player in players:
#             player.update()
        
#         if (len(players) == 0):
#             break

#         for obstacle in obstacles:
#             done = obstacle.draw(game_speed)
#             if player.rect.colliderect(obstacle.rect):
#                 player.jump()
#             if (done):
#                 obstacles.remove(obstacle)
#                 obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 0))
#                 score += 1

#         obstacle_pos = []
#         for obstacle in obstacles:
#             obstacle_pos.append(obstacle.rect.x)
#             obstacle_pos.append(obstacle.rect.y)
#         for i, player in enumerate(players):
#             output = nets[i].activate(player.X_POS / 100, player.Y_POS / 100, obstacle_pos)
#             if output[0] > 0.5 and dinosaur.rect.y == dinosaur.Y_POS:
#                 dinosaur.dino_jump = True
#                 dinosaur.dino_run = False
        

# global pop
# config = neat.config.Config(
#     neat.DefaultGenome,
#     neat.DefaultReproduction,
#     neat.DefaultSpeciesSet,
#     neat.DefaultStagnation,
#     config_path
# )
# pop = neat.Population(config)
# pop.run(eval_genomes, 10000)
