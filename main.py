"""This is the main module of the game 'Falling Things'"""

import pygame

from time import sleep

from player import Player
from obstacle import Obstacle

pygame.init()

#Creating the main window and setting caption
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Falling Things Game")

#Setting Images
ground_img = pygame.image.load("ground.png")

#Font
font = pygame.font.Font(pygame.font.get_default_font(), 32)

#Player
player = Player(400, 450, 0)

#Obstacle(s)
num_of_obstacles = 5

obstacles = []

for obstacle in range(0, num_of_obstacles):
    obstacle = Obstacle()
    obstacles.append(obstacle)

#Score
score = 0

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

    #Blocking Player Off-screen
    if player.x > 750:
        player.x = 750
    elif player.x < 0:
        player.x = 0

    for obstacle in obstacles:
        obstacle.y += obstacle.y_acc

        if obstacle.y > 475:
            obstacle.y = 0
            obstacle.reset_x()

    SCREEN.blit(ground_img, (0, 500))
    player.draw(SCREEN)

    score += 1

    for obstacle in obstacles:
        obstacle.draw(SCREEN)

        if obstacle.collide(player):
            for j in obstacles:
                j.reset_x()
            
            score = 0
            sleep(2)

    #Rendering Fonts
    #   SCREEN.blit(font.render(f"X: {player.x}", True, (0, 0, 0)), (0, 25))
    SCREEN.blit(font.render(f"Score: {score}", True, (0,0,0)), (0, 0))

    pygame.display.update()
