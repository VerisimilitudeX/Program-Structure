#### ---- SETUP ---- ####

import pygame
pygame.init()
window = pygame.display.set_mode([300, 200])


# --- Animation variables --- #

star_offset = 0
star_speed = 1
color_offset = 10
color_change = 5


#### ---- MAIN LOOP ---- ####

animating = True
while animating:

    # --- Event loop --- #
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False

    # --- Color --- #
    
    color = (255, 255, color_offset)
    color_offset += color_change
    if color_offset > 245 or color_offset < 10:
        color_change = color_change * -1


    # --- Star points --- #

    pt1 = (150, 30 + star_offset)
    pt2 = (160, 60 + star_offset)
    pt3 = (195, 60 + star_offset)
    pt4 = (165, 75 + star_offset)
    pt5 = (195, 120 + star_offset)
    pt6 = (150, 90 + star_offset)
    pt7 = (105, 120 + star_offset)
    pt8 = (135, 75 + star_offset)
    pt9 = (105, 60 + star_offset)
    pt10 = (140, 60 + star_offset)


    # --- Reverse direction at limits --- #
    
    star_offset += star_speed
    if star_offset > 50 or star_offset < 0:
        star_speed = star_speed * -1


    # --- Draw frame --- #

    window.fill((20, 0, 80))
    pygame.draw.polygon(window, color, [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10])
    pygame.display.flip()
    pygame.time.wait(20)
