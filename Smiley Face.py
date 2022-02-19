# import
import pygame
pygame.init()
window = pygame.display.set_mode([400, 400])

# set color
bg_color = (40, 20, 30)
face_color = (190, 160, 60)
black = (0, 0, 0)
mouth_color = (90, 20, 30)

# defined Rect
face_center = (200, 200)
left_eye_rect = pygame.Rect(110, 80, 40, 80)
right_eye_rect = pygame.Rect(250, 80, 40, 80)
mouth_rect = pygame.Rect(120, 260, 160, 10)

# offset
mouth_height = 10
mouth_offset = 0
mouth_opening = True

# declare while loop
drawing = True
while drawing:

    # end program if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # offset
    if mouth_opening:
        mouth_offset += 8
    else:
        mouth_offset -= 8
    mouth_rect.height = mouth_height + mouth_offset

    # end program if done
    if mouth_offset >= 50:
        mouth_opening = False
    if mouth_offset <= 0:
        mouth_opening = True

    # draw shapes
    window.fill(bg_color)
    pygame.draw.circle(window, face_color, face_center, 180)
    pygame.draw.circle(window, black, face_center, 180, 5)
    pygame.draw.ellipse(window, black, left_eye_rect)
    pygame.draw.ellipse(window, black, right_eye_rect)
    pygame.draw.ellipse(window, mouth_color, mouth_rect)
    pygame.draw.ellipse(window, black, mouth_rect, 5)
    pygame.display.flip()
    pygame.time.wait(40)
