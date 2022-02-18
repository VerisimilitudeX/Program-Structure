import pygame
pygame.init()
window = pygame.display.set_mode([600, 400])

arrow_color = (240, 230, 170)
balloon_color = (160, 20, 20)
sky_color = (100, 210, 250)

arrow_x_offset = 0
arrow_y_offset = 0
balloon_offset = 0

arrow_x_start = -40
arrow_y_start = 395
balloon_y_start = 300
balloon_rect = pygame.Rect(330, balloon_y_start, 60, 90)

arrow_x_speed = int(input("How fast should the arrow move horizontally? "))
arrow_y_speed = int(input("How fast should the arrow move vertically? "))
balloon_speed = -4

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    arrow_x_offset += arrow_x_speed
    arrow_y_offset += arrow_y_speed * -1
    balloon_offset += balloon_speed
    balloon_rect.y = balloon_y_start + balloon_offset

    window.fill(sky_color)
    pygame.draw.ellipse(window, balloon_color, balloon_rect)
    arrow_tail = (arrow_x_start + arrow_x_offset, arrow_y_start + arrow_y_offset)
    arrow_head = (arrow_x_start + arrow_x_offset + 60, arrow_y_start + arrow_y_offset - 10)
    pygame.draw.line(window, arrow_color, arrow_tail, arrow_head, 5)
    pygame.display.flip()
    pygame.time.wait(40)
