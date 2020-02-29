"""This is the main module of the game 'Falling Things'"""

import pygame

from player import *

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Falling Things Game")

#Setting Images
ground_img = pygame.image.load("ground.png")
def draw_player(x, y):
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect((x, y), (50, 50)))

#Player Variables
player = Player(400, 450, 0)
player_x = 400
player_x_acc = 0
player_y = 450

running = True
#Game Loop
while running:

    SCREEN.fill((0, 191, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("QUIT Event: Exiting window!")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.acc_x = 1
            if event.key == pygame.K_LEFT:
                player.acc_x = -1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.acc_x = 0

    player.x += player.acc_x

    SCREEN.blit(ground_img, (0, 500))
    player.draw(SCREEN)
    pygame.display.update()
