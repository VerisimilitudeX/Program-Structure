import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])

left_color = (100, 180, 240)
right_color = (100, 240, 180)

offset = 0

frames = 0

while frames <= 100:

    offset += 2

    window.fill((230, 255, 240))

    p1 = (offset, 0)
    p2 = (200 + offset, 0)
    p3 = (400 - offset, 400)
    p4 = (200 - offset, 400)

    p5 = (offset, 400)
    p6 = (200 + offset, 400)
    p7 = (400 - offset, 0)
    p8 = (200 - offset, 0)

    pygame.draw.polygon(window, right_color, [p5, p6, p7, p8])
    pygame.draw.polygon(window, left_color, [p1, p2, p3, p4])

    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1
    print(frames-1)

    if frames > 100:
        pygame.QUIT
