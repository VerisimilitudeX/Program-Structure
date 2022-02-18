import pygame
pygame.init()

window = pygame.display.set_mode([500, 500])
window.fill((255, 255, 255))

circle_x = 0
while circle_x < 500:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            circle_x = 1000
    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), (circle_x, 250), 25)
    circle_x += 5

    pygame.display.flip()

input()
