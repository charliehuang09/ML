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