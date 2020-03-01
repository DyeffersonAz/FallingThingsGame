"""Defines the player and all its methods"""

import pygame

class Player:
    """Defines Player"""

    def __init__(self, x, y, acc_x):
        self.x = x
        self.y = y
        self.acc_x = acc_x

    def draw(self, screen):
        """Puts the player on screen with given display object"""
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((self.x, self.y), (50, 50)))
