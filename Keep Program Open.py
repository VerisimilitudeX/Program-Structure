import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
ball_color = (235, 245, 255)
slope_color = (60, 70, 90)

circle_x = 22
circle_y = -22
circle_offset = 0

drawing = True
while drawing:
    if circle_offset > 400:
        drawing = False

    circle_offset += 3
    circle_center = (circle_x + circle_offset, circle_y + circle_offset)

    window.fill((180, 190, 220))
    pygame.draw.polygon(window, slope_color, [(0, 0), (0, 400), (400, 400)])
    pygame.draw.circle(window, ball_color, circle_center, 30)

    pygame.display.flip()
    pygame.time.wait(40)
