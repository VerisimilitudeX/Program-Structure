import pygame
pygame.init()

window = pygame.display.set_mode([600, 150])

circle_color = (230, 210, 250)
bg_color = (80, 60, 90)
overlay_color = (60, 40, 70)

overlay_rect = pygame.Rect(0, 0, 600, 5)
offset = 0

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    offset += 5
    offset %= 150

    window.fill(bg_color)
    overlay_rect.y = offset - 2
    pygame.draw.rect(window, overlay_color, overlay_rect)
    pygame.draw.circle(window, circle_color, (-50 + offset, 75), 50)
    pygame.draw.circle(window, circle_color, (100 + offset, 75), 50)
    pygame.draw.circle(window, circle_color, (250 + offset, 75), 50)
    pygame.draw.circle(window, circle_color, (400 + offset, 75), 50)
    pygame.draw.circle(window, circle_color, (550 + offset, 75), 50)

    pygame.display.flip()
    pygame.time.wait(40)
