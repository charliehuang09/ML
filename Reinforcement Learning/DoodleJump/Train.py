import pygame
import time
import sys
import random
import neat
import numpy as np
DISPLAY = True
generation = 0
max_score = 0
max_plot = np.array([])
mean_plot = np.array([])
pygame.init()
CLOCK = pygame.time.Clock()

SCREEN_HEIGHT = 1200
SCREEN_WIDTH = 1000
if DISPLAY:
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    SCREEN.fill((255,255,255))
    pygame.display.update()
config_path = '/Users/charlie/ML/Reinforcement Learning/DoodleJump/config.txt'

CHARECTER = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/DoodleJump/Assets/Charecter.jpeg')
CHARECTER = pygame.transform.scale(CHARECTER, (64, 64))
GREEN_OBSTACLE = pygame.image.load('/Users/charlie/ML/Reinforcement Learning/DoodleJump/Assets/Green_Obstacle.png')
GREEN_OBSTACLE = pygame.transform.scale(GREEN_OBSTACLE, (128, 32))
def linear(x):
    return x

class Obstacle:
    def __init__(self, img, x, y, id_):
        self.img = img
        self.id = id_
        self.rect = pygame.Rect(x, y, img.get_width(), img.get_height())

    def draw(self, offset):
        global DISPLAY
        self.rect.y -= offset
        if DISPLAY:
            SCREEN.blit(self.img, (self.rect.x, self.rect.y))
        return self.rect.y > 1200

class Player:
    X_POS = 500
    Y_POS = 1000
    JUMP_VEL = 8.5

    def __init__(self, img, obstacle):
        self.reward = self.Y_POS
        self.img = img
        self.xStrength = 4
        self.yStrength = 25
        self.xVelocity = 0
        self.yVelocity = -20
        self.gravity = 1
        self.y_limit = 500
        self.x_min = -50
        self.x_max = 50
        self.score = 0
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.obstacle_id = obstacle
    
    def update(self, speed):
        offset = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        self.xVelocity *= 0.9
        self.yVelocity *= 0.99
        self.yVelocity += self.gravity
        self.xVelocity = max(self.xVelocity, self.x_min)
        self.xVelocity = min(self.xVelocity, self.x_max)
        self.X_POS += self.xVelocity
        self.Y_POS += self.yVelocity
        self.Y_POS -= speed
        if self.Y_POS < self.y_limit:
            offset = self.Y_POS - self.y_limit
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        return offset

    def update_obstacle(self, obstacle):
        self.obstacle_id = max(self.obstacle_id, obstacle)

    def jump(self):
        self.yVelocity = -self.yStrength
    
    def left(self):
        self.xVelocity = min(0, self.xVelocity)
        self.xVelocity -= self.xStrength
    
    def right(self):
        self.xVelocity = max(0, self.xVelocity)
        self.xVelocity += self.xStrength

    def draw(self, offset):
        global DISPLAY
        self.Y_POS -= offset
        self.rect.y = self.Y_POS
        if DISPLAY:
            SCREEN.blit(self.img, (self.rect.x, self.rect.y))

# obstacles = []
# obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 1100, 0))
# obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 900, 1))
# obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 700, 2))
# obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 500, 3))
# obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 300, 4))
# obstacles.append(Obstacle(GREEN_OBSTACLE, 500, 100, 5))
# player = Player(CHARECTER, 0)
# while(True):
#     CLOCK.tick(5)
#     userInput = pygame.key.get_pressed()
#     if userInput[pygame.K_a]:
#         player.left()
#     if userInput[pygame.K_d]:
#         player.right()
#     if userInput[pygame.K_w]:
#         player.jump()
#     SCREEN.fill((255, 255, 255))
#     offset = player.update(0)
#     player.draw(offset)
#     for obstacle in obstacles:
#         print(player.obstacle_id)
#         if player.rect.colliderect(obstacle.rect) and player.yVelocity > 0:
#             player.jump()
#             player.update_obstacle(obstacle.id)
#         done = obstacle.draw(offset)
#         if (done):
#             obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(200, 800), 0, obstacle.id + 6))
#             obstacles.remove(obstacle)
#     pygame.display.update()

def eval_genomes(genomes, config):
    global obstacles, players, ge, nets, generation, max_score, max_plot, mean_plot, DISPLAY
    obstacles = []
    players = []
    ge = []
    nets = []
    tot_score = 0

    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(100, 900), 1100, 0))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(100, 900), 900, 1))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(100, 900), 700, 2))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(100, 900), 500, 3))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(100, 900), 300, 4))
    obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(100, 900), 100, 5))
    for genome_id, genome in genomes:
        players.append(Player(CHARECTER, 0))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    run = True
    while run:
        # CLOCK.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if DISPLAY:
            SCREEN.fill((255,255,255))
        offset = 0
        for player in players:
            offset = min(offset, player.update(-1))
        for player in players:
            player.draw(offset)

        if (len(players) == 0):
            break

        for obstacle in obstacles:
            done = obstacle.draw(offset - 1)
            for player in players:
                if player.rect.colliderect(obstacle.rect) and player.yVelocity > 0:
                    player.jump()
                    player.update_obstacle(obstacle.id)
            if (done):
                obstacles.append(Obstacle(GREEN_OBSTACLE, random.randint(200, 800), 0, obstacle.id + 6))
                obstacles.remove(obstacle)

        for i, player in enumerate(players):
            if player.Y_POS > 1200:
                ge[i].fitness = player.obstacle_id
                max_score = max(max_score, ge[i].fitness)
                ge.pop(i)
                players.pop(i)
                tot_score += player.obstacle_id
                continue
            idx = -1
            for j, obstacle in enumerate(obstacles):
                if obstacle.id == player.obstacle_id:
                    idx = j
                    break
            output = nets[i].activate(((obstacles[idx].rect.x - player.X_POS) / 10, (obstacles[idx].rect.y - player.Y_POS) / 10, (obstacles[idx + 1].rect.x - player.X_POS) / 10, (obstacles[idx + 1].rect.y - player.Y_POS) / 10, player.yVelocity))
            move = output.index(max(output))
            if move == 0:
                player.left()
            if move == 1:
                player.right()
        
        if DISPLAY:
            pygame.display.update()

    generation += 1
    print(f"generation: {generation} max score: {max_score} mean score: {tot_score / len(genomes)} population size: {len(genomes)}")
    mean_plot = np.append(mean_plot, tot_score / len(genomes))
    max_plot = np.append(max_plot, max_score)
    max_score = 0
    np.save("max.npy", max_plot)
    np.save("mean.npy", mean_plot)



global pop
config = neat.config.Config(
    neat.DefaultGenome,
    neat.DefaultReproduction,
    neat.DefaultSpeciesSet,
    neat.DefaultStagnation,
    config_path
)
config.genome_config.add_activation('linear', linear)
pop = neat.Population(config)
pop.run(eval_genomes, 100000)
np.save("max.npy", max_plot)
np.save("mean.npy", mean_plot)

#random score: 1200
#after 50 gen max: 2000
#378 max: 5000