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
                