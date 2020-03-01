"""This is the main module of the game 'Falling Things'"""

import pygame

from player import Player

pygame.init()

#Creating the main window and setting caption
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Falling Things Game")

#Setting Images
ground_img = pygame.image.load("ground.png")

#Fonts
debug_font = pygame.font.Font(pygame.font.get_default_font(), 32)

#Player Variables
player = Player(400, 450, 0)


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

    #Rendering Fonts
    SCREEN.blit(debug_font.render(f"X: {player.x}", True, (0, 0, 0)), (0, 0))

    SCREEN.blit(ground_img, (0, 500))
    player.draw(SCREEN)
    pygame.display.update()
