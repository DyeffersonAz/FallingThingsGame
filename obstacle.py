"""Defines the obstacle which the player needs to avoid"""

from random import randint

import pygame

class Obstacle:
    """Class to define the Obstacle"""

    def __init__(self):
        """Initializing the obstacle randomly in the x and 0 in y"""
        self.x = randint(0, 800)
        self.y = 0
        self.y_acc = randint(1, 3)

    def draw(self, SCREEN):
        """Drawing obstacle as a circle"""
        pygame.draw.circle(SCREEN, (255, 211, 0), (self.x, self.y), 25)
    
    def reset_x(self):
        self.x = randint(0, 800)
