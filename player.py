import pygame

class Player:

    def __init__(self, x, y, acc_x):
        self.x = x
        self.y = y
        self.acc_x = acc_x
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((self.x, self.y), (50, 50)))