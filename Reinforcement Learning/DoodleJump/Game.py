import pygame
import time
import sys
import random
import neat
from scipy.special import softmax
generation = 0
max_score = 0
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
        self.reward = self.Y_POS
        self.img = img
        self.xStrength = 1.5
        self.yStrength = 30
        self.xVelocity = 0
        self.yVelocity = -20
        self.gravity = 1
        self.y_limit = 400
        self.x_min = -50
        self.x_max = 50
        self.score = 0
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
    
    def update(self, speed):
        offset = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
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

def eval_genomes(genomes, config):
    clock = pygame.time.Clock()
    global game_speed, x_pos_bg, y_pos_bg, obstacles, players, ge, nets, points, generation, max_score
    obstacles = []
    players = []
    ge = []
    nets = []
    score = 0
    offset = 0
    game_speed = -1

    obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 1100))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 900))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 700))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 500))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 300))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 100))
    for genome_id, genome in genomes:
        players.append(Player(CHARECTER))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    run = True
    while run:
        offset += game_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((255,255,255))
        for player in players:
            player.update(game_speed)
        
        if (len(players) == 0):
            break

        for obstacle in obstacles:
            done = obstacle.draw(game_speed)
            for player in players:
                if player.rect.colliderect(obstacle.rect):
                    player.jump()
            if (done):
                obstacles.remove(obstacle)
                obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(0, 1000), 0))
                score += 1

        for i, player in enumerate(players):
            if player.Y_POS > 12000:
                ge[i].fitness = player.reward
                max_score = max(max_score, player.reward)
                players.remove(player)
                continue
            player.reward = max(player.reward, player.Y_POS - offset)
            output = nets[i].activate((((obstacles[0].rect.x - player.rect.x) / 100, (obstacles[1].rect.x - player.rect.x) / 100, (obstacles[2].rect.x - player.rect.x) / 100, (obstacles[3].rect.x - player.rect.x) / 100, (obstacles[4].rect.x - player.rect.x) / 100, (obstacles[5].rect.x - player.rect.x) / 100, (obstacles[0].rect.y - player.rect.y) / 100, (obstacles[1].rect.y - player.rect.y) / 100, (obstacles[2].rect.y - player.rect.y) / 100, (obstacles[3].rect.y - player.rect.y) / 100, (obstacles[4].rect.y - player.rect.y) / 100, (obstacles[5].rect.y - player.rect.y) / 100, player.rect.x / 100, player.rect.y / 100)))
            move = output.index(max(output))
            if move == 0:
                player.left()
            if move == 1:
                player.right()
        # print(offset)
                
        pygame.display.update()
    generation += 1
    print(f"generation: {generation} score: {max_score}")
    max_score = 0
        

global pop
config = neat.config.Config(
    neat.DefaultGenome,
    neat.DefaultReproduction,
    neat.DefaultSpeciesSet,
    neat.DefaultStagnation,
    config_path
)
pop = neat.Population(config)
pop.run(eval_genomes, 1000000)
