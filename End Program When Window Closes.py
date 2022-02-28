# import and initialize
import pygame
pygame.init()
# set window
window = pygame.display.set_mode([400, 400])
window.fill((255, 255, 255))
# break loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
