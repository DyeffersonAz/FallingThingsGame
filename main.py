"""This is the main module of the game 'Falling Things'"""

import pygame

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Falling Things Game")

#Setting Images
ground_img = pygame.image.load("ground.png")
def draw_player(x, y):
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect((x, y), (50, 50)))

running = True
#Game Loop
while running:

    SCREEN.fill((0, 191, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("QUIT Event: Exiting window!")

    SCREEN.blit(ground_img, (0, 500))
    draw_player(400, 450)
    pygame.display.update()
