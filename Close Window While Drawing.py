import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

red = 0
blue = 128
becoming_red = True

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if red >= 128:
        becoming_red = False
    if blue >= 128:
        becoming_red = True

    if becoming_red:
        red += 2
        blue -= 2
    else:
        red -= 2
        blue += 2

    bars = 0
    while bars <= 100:
        color = (red + bars, 20, blue + bars)
        pygame.draw.line(window, color, (bars * 4, 0), (bars * 4, 400), 4)
        bars += 1

    pygame.display.flip()
    pygame.time.wait(40)
